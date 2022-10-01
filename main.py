from fastapi import FastAPI, HTTPException
import json

# Imports
from src import filters


# Initiating a FastAPI application
app = FastAPI(
    title="College API",
    description="Fetch the details of Indian Colleges",
    version="1",
    terms_of_service="http://example.com/terms/",
    contact={
        "name": "Clueless Community",
        "url": "https://www.clueless.tech/",
        "email": "https://www.clueless.tech/contact-us",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    }
)


@app.get('/')
async def home():

    return {
        "Status": "Server running sucessfully"
    }


@app.get('/engineering_colleges')
def enfineeringColleges():

    try:
        with open(r'data\allEngineeringColleges.json', 'r') as file:
            output = json.load(file)
    except:
        raise HTTPException(status_code=404)

    return output


@app.get('/engineering_colleges/nirf')
def engineeringCollegesNirf():

    try:
        with open(r'data\nirfEngineeringColleges.json', 'r') as file:
            output = json.load(file)
    except:
        raise HTTPException(status_code=503)

    return output



@app.get('/engineering_colleges/state={state}')
async def engineeringCollegesByState(state: str | None = None):

    name_of_state = state.lower()

    try:
        response = filters.engineering_colleges_by_state(name_of_state)
        if len(response) == 0:
            raise HTTPException(status_code=404, detail='State not found')
        return response
    except Exception as e:
        raise HTTPException(status_code=404, detail='State  not found')



@app.get('/engineering_colleges/city={city}')
async def engineeringCollegesByCity(city: str | None = None):
    name_of_the_city = city.lower()
    try:
        response = filters.engineering_colleges_by_city(name_of_the_city)
        if len(response) == 0:
            raise HTTPException(status_code=404, detail='City not found')
        return response

    except Exception as e:
        raise HTTPException(status_code=404, detail='City not found')

@app.get('/medical_colleges')
def medicalColleges():
    try:
        with open(r'data\allMedicalColleges.json', 'r') as file:
            output = json.load(file)
    except:
        raise HTTPException(status_code=404)

    return output

@app.get('/medical_colleges/nirf')
def medicalColleges():
    try:
        with open(r'data\nirfMedicalColleges.json', 'r') as file:
            output = json.load(file)
    except:
        raise HTTPException(status_code=503)

    return output