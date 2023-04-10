import threading
import json
from collections import namedtuple
from json import JSONEncoder

# import "packages" from flask
# from flask import render_template  # import render_template from "public" flask libraries

# import "packages" from "this" project
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

# @app.context_processor
def getNutritionInfo(foodName):
    url = "https://nutrition-by-api-ninjas.p.rapidapi.com/v1/nutrition"

    querystring = {"query": foodName}

    headers = {
        "X-RapidAPI-Key": "8ca68e698emsh077b34dcb5cedc7p176bfdjsn4a11c2cb1bef",
        "X-RapidAPI-Host": "nutrition-by-api-ninjas.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    # foodFromResponse = json.dumps(response.text, indent=4, cls=FoodEncoder)

    foodObj = json.loads(response.text, object_hook=customFoodDecoder)

    # print(studObj.maxScore)
    # # print(foodFromResponse.maxScore)
    print(foodObj)
    return foodObj #render_template("index.html", studObj = studObj)

app = Flask(__name__)
SESSION_TYPE = 'filesystem'
app.config.from_object(__name__)
Session(app)
@app.route('/')
def home():
    session["calorieTotal"] = 0
    # add a list here by doing session[<name of food list>] and set it equal to empty list
    session["nameFoodList"] = []
    return render_template("index.html", studObj = 0)

# @app.route("/home")
# def home2():
#     return render_template("index.html")

@app.route("/result", methods = ['POST', "GET"])
def result():
    # use session[<food name>].append to add to food list
    output = request.form.to_dict()
    currentFood = output["currentFood"]
    currentFood = getNutritionInfo(currentFood)
    if not "calorieTotal" in session:
        session["calorieTotal"] = 0
    # add if statement to check if <food name> is in session or not, in if statement repeat the code in home() 
    if not "nameFoodList" in session: 
        session["nameFoodList"] = []
    
    session["nameFoodList"].append((output["currentFood"], currentFood[0].calories))

    session["calorieTotal"] = session["calorieTotal"] + currentFood[0].calories
    
    return render_template("index.html", currentFood = session["calorieTotal"], calorieList=session["calorieList"], foodList = session["nameFoodList"])

# if __name__ == '__main__':
#     app.run(debug=True,port=8086)


@app.errorhandler(404)  # catch for URL not found
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404

@app.route('/')  # connects default URL to index() function
def index():
    return render_template("index.html")

# @app.before_first_request
# def activate_job():  # activate these items 
    

# this runs the application on the development server
if __name__ == "__main__":
    # change name for testing
    # from flask_cors import CORS
    # cors = CORS(app)
    app.run(debug=True, host="0.0.0.0", port="8086")


# calorieList = []
# for i in objects:
#     string = getstring(i)
#     calorieList.append(string)