import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
import joblib

anime = pd.read_csv("./server/anime_preprocessed.csv")
y=anime['Rating']
anime=anime.drop('Rating',axis=1)
X_train, X_test, y_train, y_test = train_test_split(anime.values, y, test_size=0.2)
rf_model = RandomForestRegressor(n_estimators=100, criterion='squared_error', random_state=42)
rf_model.fit(X_train, y_train)
joblib.dump(rf_model, "modele.pkl")
joblib.dump(anime.columns, "columns.pkl")
print("hey")
