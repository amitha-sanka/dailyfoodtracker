import threading
import json
from collections import namedtuple
from json import JSONEncoder


from __init__ import app  # Definitions initialization
from flask import Flask,render_template,request, session
from flask_session import Session

import requests
from model.food_models import FoodEncoder, customFoodDecoder, Food

"""
These object can be used throughout project.
1.) Objects from this file can be included in many blueprints
2.) Isolating these object definitions avoids duplication and circular dependencies
"""



currentFood = None

def getNutritionInfo(foodName):
    url = "https://nutrition-by-api-ninjas.p.rapidapi.com/v1/nutrition"

    querystring = {"query": foodName}

    headers = {
        "X-RapidAPI-Key": "8ca68e698emsh077b34dcb5cedc7p176bfdjsn4a11c2cb1bef",
        "X-RapidAPI-Host": "nutrition-by-api-ninjas.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    foodObj = json.loads(response.text, object_hook=customFoodDecoder)

    print(foodObj)
    return foodObj 

app = Flask(__name__)
SESSION_TYPE = 'filesystem'
app.config.from_object(__name__)
Session(app)
@app.route('/')
def home():
    session["calorieTotal"] = 0
    session["nameFoodList"] = []
    return render_template("index.html", studObj = 0)



@app.route("/result", methods = ['POST', "GET"])
def result():
    output = request.form.to_dict()
    currentFood = output["currentFood"]
    currentFood = getNutritionInfo(currentFood)
    if not "calorieTotal" in session:
        session["calorieTotal"] = 0
    if not "nameFoodList" in session: 
        session["nameFoodList"] = []
    
    session["nameFoodList"].append((output["currentFood"], currentFood[0].calories))

    session["calorieTotal"] = session["calorieTotal"] + currentFood[0].calories
    
    return render_template("index.html", currentFood = session["calorieTotal"], calorieList=session["calorieList"], foodList = session["nameFoodList"])




@app.errorhandler(404)  
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/') 
def index():
    return render_template("index.html")

    
if __name__ == "__main__":
    
    app.run(debug=True, host="0.0.0.0", port="8086")

