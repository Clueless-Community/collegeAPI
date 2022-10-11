from fastapi import FastAPI, HTTPException
import json
import os

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
        "name": "GPL-3.0 license",
        "url": "https://github.com/Clueless-Community/collegeAPI/blob/main/LICENSE.md",
    }
)
def colleges_by_state_or_city(field,region,region_list):
    response = []
    for i in region_list:
        i = i.replace(" ", "").lower()
        if(field=='engineering' and region=='state'):
            response.extend(filters.engineering_colleges_by_state(i))
        elif(field=='engineering' and region=='city'):
            response.extend(filters.engineering_colleges_by_city(i))
        elif(field=='medical' and region=='state'):
            response.extend(filters.medical_colleges_by_state(i))
        elif(field=='medical' and region=='city'):
            response.extend(filters.medical_colleges_by_city(i))
        elif(field=='management' and region=='state'):
            response.extend(filters.management_colleges_by_state(i))
        elif(field=='management' and region=='city'):
            response.extend(filters.management_colleges_by_city(i))
    return response
@app.get('/')
async def home():

    return {
        "Status": "Server running sucessfully"
    }


@app.get('/engineering_colleges')
def engineeringColleges():
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
async def engineeringCollegesByState(state: str or None = None):
    # multiple states will be seperated by '&' like Maharastra&Andhra Pradesh
    states_list = [x.strip() for x in state.split('&')]
    try:
        response =colleges_by_state_or_city('engineering','state',states_list)
        if len(response) == 0:
            raise HTTPException(status_code=404, detail='State not found')
        return response
    except Exception as e:
        raise HTTPException(status_code=404, detail='State  not found')


@app.get('/engineering_colleges/city={city}')
async def engineeringCollegesByCity(city: str or None = None):
    city_list = [x.strip() for x in city.split('&')]
    try:
        response =colleges_by_state_or_city('engineering','city',city_list)
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


@app.get('/medical_colleges/state={state}')
def medicalCollegesByState(state: str or None = None):
    # multiple states will be seperated by '&' like Maharastra&Andhra Pradesh
    states_list = [x.strip() for x in state.split('&')]
    try:
        response =colleges_by_state_or_city('medical','state',states_list)
        if len(response) == 0:
            raise HTTPException(status_code=404, detail='State not found')
        return response

    except Exception as e:
        raise HTTPException(
            status_code=404, detail='Some error occured, please try again')


@app.get('/medical_colleges/city={city}')
async def medicalCollegesByCity(city: str or None = None):
    city_list = [x.strip() for x in city.split('&')]
    try:
        response =colleges_by_state_or_city('medical','city',city_list)
        if len(response) == 0:
            raise HTTPException(status_code=404, detail='City not found')
        return response

    except Exception as e:

        raise HTTPException(
            status_code=404, detail='Some error occured, please try again')


@app.get('/management_colleges')
def managementColleges():
    try:
        with open(r'data\allManagementColleges.json', 'r') as file:
            output = json.load(file)
    except:
        raise HTTPException(status_code=404)

    return output


@app.get('/management_colleges/nirf')
def managementCollegesNirf():

    try:
        with open(r'data\nirfManagementColleges.json', 'r') as file:
            output = json.load(file)
    except:
        raise HTTPException(status_code=503)

    return output


@app.get('/management_colleges/city={city}')
async def managementCollegesByCity(city: str or None = None):
    city_list = [x.strip() for x in city.split('&')]
    try:
        response =colleges_by_state_or_city('management','city',city_list)
        if len(response) == 0:
            raise HTTPException(status_code=404, detail='City not found')
        return response
    except Exception as e:
        raise HTTPException(
            status_code=404, detail='Some error occured, please try again')


@app.get('/management_colleges/state={state}')
async def managementCollegesByState(state: str or None = None):
    states_list = [x.strip() for x in state.split('&')]
    try:
        response =colleges_by_state_or_city('management','state',states_list)
        if len(response) == 0:
            raise HTTPException(status_code=404, detail='State not found')
        return response

    except Exception as e:
        raise HTTPException(
            status_code=404, detail='Some error occured, please try again')


@app.get('/colleges')
def allColleges():

    try:
        with open(r'data\allEngineeringColleges.json', 'r') as file:
            output = json.load(file)
    except:
        raise HTTPException(status_code=404)

    return output


@app.get('/colleges/nirf')
def nirfCollegesRanked():

    try:
        with open(r'data\nirfCollegesRanked.json', 'r') as file:
            output = json.load(file)
    except:
        raise HTTPException(status_code=404)

    return output


@app.get('/pharmacy_colleges')
def allParticipatingPharmacyCollege():

    try:
        with open(r'data\allParticipatingPharmacyCollege.json', 'r') as file:
            output = json.load(file)
    except:
        raise HTTPException(status_code=404)

    return output


@app.get('/pharmacy_colleges/nirf')
def pharmacyCollegesNirf():

    try:
        with open(r'data\nirfPharmacyColleges.json', 'r') as file:
            output = json.load(file)
    except:
        raise HTTPException(status_code=503)

    return output


@app.get('/dental_colleges/nirf')
def nirf_dental_colleges():

    try:
        with open(os.path.join(os.getcwd(), "data", "nirfDentalColleges.json")) as file:
            output = json.load(file)
            return output
    except:
        raise HTTPException(status_code=500)
    
@app.get('/law_colleges/nirf')
def nirf_dental_colleges():

    try:
        with open(os.path.join(os.getcwd(), "data", "nirfLawCollegesRanked.json")) as file:
            output = json.load(file)
            return output
    except:
        raise HTTPException(status_code=500)

@app.get('/architecture_colleges/nirf')
def architectureCollegesNirf():

    try:
        with open(r'data\nirfArchitectureColleges.json', 'r') as file:
            output = json.load(file)
    except:
        raise HTTPException(status_code=503)

    return output


@app.get('/agriculture_colleges/')
def agriculture_colleges():

    try:
        with open(r'data/allagriculturecolleges.json', 'r') as file:
            output = json.load(file)
    except:
        raise HTTPException(status_code=404)

    return output