from fastapi import FastAPI
import json


app = FastAPI()

@app.get('/')
def home():

    return {
        "Status":"Server running sucessfully"
    }

@app.get('/engineeringColleges/nirf')
def engineeringColleges():

    with open('./jsonFiles/engineeringCollegesNirf.json', 'r') as file:
        output = json.load(file)

    return output