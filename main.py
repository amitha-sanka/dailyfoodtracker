import threading
import json
from collections import namedtuple
from json import JSONEncoder
# import "packages" from flask
# from flask import render_template  # import render_template from "public" flask libraries

# import "packages" from "this" project
from __init__ import app  # Definitions initialization
from flask import Flask,render_template,request

from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import requests
from model.food_models import FoodEncoder, customFoodDecoder, Food

"""
These object can be used throughout project.
1.) Objects from this file can be included in many blueprints
2.) Isolating these object definitions avoids duplication and circular dependencies
"""

# # Setup of key Flask object (app)
app = Flask(__name__)

# @app.context_processor
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
    return render_template("index.html", studObj = studObj)

app = Flask(__name__)
@app.route('/')
def home():
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
    return render_template("index.html", studObj = studObj[0].name)
# @app.route("/home")
# def home2():
#     return render_template("index.html")

# @app.route("/result", methods = ['POST', "GET"])
# def result():
#     output = request.form.to_dict()
#     name = output["name"]

#     return render_template("index.html", name = name)

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
