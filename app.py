from flask import Blueprint, Flask, jsonify, request
from prometheus_client import make_wsgi_app
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.serving import run_simple
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import joblib
from flask_cors import CORS

from flask_prometheus_metrics import register_metrics


pred_model = joblib.load("modele.pkl")
model_emb = SentenceTransformer('distilbert-base-nli-mean-tokens')
columns = joblib.load("columns.pkl")
def transform_input(title,genre,synopsis,typ,producer,studio, model, columns) :
    #embed phrases
    table = genre.split("|") + typ.split("|") +producer.split("|") + studio.split("|")
    zero_vector = np.ones((1, 768))
    emb_title = model.encode([title] , show_progress_bar=True)
    cos_title = cosine_similarity(zero_vector, emb_title)[0][0]
    emb_synopsis = model.encode([synopsis], show_progress_bar=True)
    cos_synopsis = cosine_similarity(zero_vector, emb_synopsis)[0][0]
    col = [1 if i in table else 0 for i in columns]
    col[0] = cos_title
    col[1] = cos_synopsis
    return col

#
# Constants
#

CONFIG = {"version": "v0.1.2", "config": "staging"}
MAIN = Blueprint("main", __name__)
CORS(MAIN, resources={r'/*': {'origins': '*'}})

#
# Main app
#

@MAIN.route("/")
def index():
       return "This is the main page."


@MAIN.route("/predict")
def predict():
    global model_emb,columns, pred_model
    title = request.args.get("name")
    genre = request.args.get("genre")
    description = request.args.get("description")
    typ = request.args.get("type")
    producer = request.args.get("producer")
    studio = request.args.get("studio")
    return jsonify(str(pred_model.predict([transform_input(title, genre, description,typ, producer, studio, model_emb,columns)])[0])+"/10")



def register_blueprints(app):
       """
       Register blueprints to the app
       """
       app.register_blueprint(MAIN)


def create_app(config):
       """
       Application factory
       """
       app = Flask(__name__)

       register_blueprints(app)
       register_metrics(app, app_version=config["version"], app_config=config["config"])
       return app


#
# Dispatcher
#


def create_dispatcher() :
       """
       App factory for dispatcher middleware managing multiple WSGI apps
       """
       main_app = create_app(config=CONFIG)
       return DispatcherMiddleware(main_app.wsgi_app, {"/metrics": make_wsgi_app()})


#
# Run
#

if __name__ == "__main__":
       run_simple(
       "0.0.0.0",
       5000,
       create_dispatcher(),
       use_reloader=True,
       use_debugger=True,
       use_evalex=True,
       )