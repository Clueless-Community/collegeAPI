from fastapi import FastAPI, HTTPException
import json

# Imports
from helpers.nirfEngineeringCollegeFilter import *

# Initiating a FastAPI application
app = FastAPI()


@app.get('/')
async def home():

    return {
        "Status":"Server running sucessfully"
    }


@app.get('/engineeringColleges')
async def enfineeringColleges():

    try:

        with open('./data/allEngineeringColleges.json', 'r') as file:
            output = await json.load(file)
    except:
        output = {
            "Status":"Error at server side"
        }

    return output

@app.get('/engineeringColleges/nirf')
async def engineeringCollegesNirf():

    try:
        with open('./data/engineeringCollegesNirf.json', 'r') as file:
            output = await json.load(file)
    except:
        return {
            "Status":"Error at server side"
        }

    return output


@app.get('/engineeringColleges/nirf/city={city}')
async def engineeringCollegesByCity(city: str | None = None):

    # Capitalizing first letter entered by the user
    name_of_city = city.title()

    try:
        output = searchByCity(name_of_city)
    except Exception as e:
        print(e)
        return {
            "Status":"Error at server side"
        }

    return output

@app.get('/engineeringColleges/nirf/state={state}')
async def engineeringCollegesByState(state: str | None = None):

    # Chnaging the output in lowercase
    name = state.lower()
    
    try:
        output = await searchByState(name)
    except:
        return {
            "Status":"Error at server side"
        }

    return output