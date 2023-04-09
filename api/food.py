# from flask import Blueprint, jsonify 
# from flask_restful import Api, Resource # used for REST API building

# import requests

# food_api = Blueprint('food_api', __name__,
#                    url_prefix='/api/food')
# api = Api(food_api)

# url = "https://text-translator2.p.rapidapi.com/getLanguages"

# headers = {
# 	"X-RapidAPI-Key": "8ca68e698emsh077b34dcb5cedc7p176bfdjsn4a11c2cb1bef",
# 	"X-RapidAPI-Host": "nutritionix-api.p.rapidapi.com"
# }

# response = requests.request("GET", url, headers=headers)

# print(response.text)

import requests
from flask import *
from functools import wraps
import sqlite3

app = Flask(__name__)
@app.route('/')
def home():
   return render_template('index.html')


def getNutritionInfo(foodName):
    url = "https://nutritionix-api.p.rapidapi.com/v1_1/search/"+foodName

    querystring = {"fields":"item_name,item_id,brand_name,nf_calories,nf_total_fat"}

    headers = {
        "X-RapidAPI-Key": "8ca68e698emsh077b34dcb5cedc7p176bfdjsn4a11c2cb1bef",
        "X-RapidAPI-Host": "nutritionix-api.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)

getNutritionInfo("Oreo")