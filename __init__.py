from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import requests
from flask import *
from model.food_models import FoodEncoder, customFoodDecoder, Food

"""
These object can be used throughout project.
1.) Objects from this file can be included in many blueprints
2.) Isolating these object definitions avoids duplication and circular dependencies
"""

# # Setup of key Flask object (app)
app = Flask(__name__)

@app.context_processor
def getNutritionInfo():
    url = "https://nutrition-by-api-ninjas.p.rapidapi.com/v1/nutrition"

    querystring = {"query":"1lb brisket"}

    headers = {
        "X-RapidAPI-Key": "8ca68e698emsh077b34dcb5cedc7p176bfdjsn4a11c2cb1bef",
        "X-RapidAPI-Host": "nutrition-by-api-ninjas.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    # foodFromResponse = json.dumps(response.text, indent=4, cls=FoodEncoder)

    studObj = json.loads(response.text, object_hook=customFoodDecoder)

    # print(studObj.maxScore)
    # # print(foodFromResponse.maxScore)
    print(studObj)
    return dict(food=studObj)

app.jinja_env.globals.update(getNutritionInfo=getNutritionInfo)

getNutritionInfo()
print("hello world")
