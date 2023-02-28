import requests
import unittest
import datetime

class TestMethods(unittest.TestCase):
    def ten_good_req_one_min(self) :
        start = datetime.datetime.now()
        for i in range(10):
            w = requests.get("http://127.0.0.1:5000/predict", params= {"name" : "Avenger", 
              "genre" : "Adventure|Fantasy|Sci-Fi|Shounen", 
              "description" :"Mars has been colonized and is a world where children have been replaced by robot servants known as ""dolls."" Layla is a skilled fighter with a tragic past who travels about the world. Her companions are Nei, a strange and unique doll with some unknown ties to Layla, and Speedy, who is a doll breeder. The founders of Mars see the trio as a threat to their world, and each time they attack Layla and Nei a bit more of their mysterious past and future is revealed.",
              "type" : "TV", 
              "producer" : "Production I.G", 
              "studio" : "Bee Train|Xebec"})
            self.assertEqual(w.status_code, 200)
        stop = datetime.datetime.now() - start
        self.assertTrue(stop.total_seconds < 60)

    def test_model(self):
        w = requests.get("http://127.0.0.1:5000/predict", params= {"name" : "Avenger", 
              "genre" : "Adventure|Fantasy|Sci-Fi|Shounen", 
              "description" :"Mars has been colonized and is a world where children have been replaced by robot servants known as ""dolls."" Layla is a skilled fighter with a tragic past who travels about the world. Her companions are Nei, a strange and unique doll with some unknown ties to Layla, and Speedy, who is a doll breeder. The founders of Mars see the trio as a threat to their world, and each time they attack Layla and Nei a bit more of their mysterious past and future is revealed.",
              "type" : "TV", 
              "producer" : "Production I.G", 
              "studio" : "Bee Train|Xebec"})
        note = float(w.text[1:].split("/")[0])
        self.assertTrue(abs(note - 5.97)<1)

if __name__ == '__main__':
    unittest.main()