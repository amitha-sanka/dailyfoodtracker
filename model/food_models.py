import json
from collections import namedtuple
from json import JSONEncoder


class Food:
    def __init__(self, name, calories, servingSize, fatTotal, fatSat, protein, sodium, potassium, cholestrol, carbs, fiber, sugar): 
        self.name, self.calories, self.servingSize, self.fatTotak, self.fatSat, self.protein, self.sodium, self.potassium, self.cholestrol, self.carbs, self.fiber, self.sugar =  name, calories, servingSize, fatTotal, fatSat, protein, sodium, potassium, cholestrol, carbs, fiber, sugar


class FoodEncoder(JSONEncoder):
        def default(self, o):
            return o.__dict__
        
def customFoodDecoder(foodDict):
    return namedtuple('X', foodDict.keys())(*foodDict.values())
