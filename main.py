from fastapi import FastAPI
import json

# Imports
from utills.nirfEngineeringCollegeFilter import *

# Initiating a FastAPI application
app = FastAPI()


@app.get('/')
def home():

    return {
        "Status":"Server running sucessfully"
    }


@app.get('/engineeringColleges/nirf')
def engineeringColleges():

    try:
        with open('./jsonFiles/engineeringCollegesNirf.json', 'r') as file:
            output = json.load(file)
    except:
        return {
            "Status":"Server at server side"
        }

    return output


@app.get('/engineeringColleges/nirf/city={city}')
def engineeringCollegesByCity(city):

    # Capitalizing first letter entered by the user
    name_of_city = city.title()

    try:
        output = searchByCity(name_of_city)
    except:
        return {
            "Status":"Error at server side"
        }

    return output

@app.get('/engineeringColleges/nirf/state={state}')
def engineeringCollegesByState(state):

    # Chnaging the output in lowercase
    name = state.lower()
    
    try:
        output = searchByState(name)
    except:
        return {
            "Status":"Error at server side"
        }

    return output