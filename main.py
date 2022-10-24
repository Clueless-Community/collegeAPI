# Imports
from curses import pair_number
from fastapi import FastAPI, HTTPException
from numpy import number, typename
import numpy
from pandas import array
from src import filters
import json
import os
import aiofiles
from starlette.responses import FileResponse

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

favicon_path = "favicon.ico"
app.get('/favicon.ico', include_in_schema=False)


def favicon():
    return FileResponse(favicon_path)


# Homepage
@app.get('/')
async def home():

    return {
        "title": "College API",
        "description": "Fetch the details of Indian Colleges",
        "version": "1",
        "contact": {
            "name": "Clueless Community",
            "url": "https://www.clueless.tech/",
            "email": "https://www.clueless.tech/contact-us",
        },
        "license_info": {
            "name": "GPL-3.0 license",
            "url": "https://github.com/Clueless-Community/collegeAPI/blob/main/LICENSE.md",
        }
    }


# Filter Function
def colleges_by_state_or_city(field, region, region_list):
    response = []
    for i in region_list:
        i = i.replace(" ", "").lower()
        if(field == 'engineering' and region == 'state'):
            response.extend(filters.engineering_colleges_by_state(i))
        elif(field == 'engineering' and region == 'city'):
            response.extend(filters.engineering_colleges_by_city(i))
        elif(field == 'medical' and region == 'state'):
            response.extend(filters.medical_colleges_by_state(i))
        elif(field == 'medical' and region == 'city'):
            response.extend(filters.medical_colleges_by_city(i))
        elif(field == 'management' and region == 'state'):
            response.extend(filters.management_colleges_by_state(i))
        elif(field == 'management' and region == 'city'):
            response.extend(filters.management_colleges_by_city(i))
        elif(field == 'research' and region == 'state'):
            response.extend(filters.research_colleges_by_state(i))
        elif(field == 'research' and region == 'city'):
            response.extend(filters.research_colleges_by_city(i))
        elif(field == 'dental' and region == 'state'):
            response.extend(filters.dental_colleges_by_state(i))
        elif(field == 'dental' and region == 'city'):
            response.extend(filters.dental_colleges_by_city(i))
        elif(field == 'pharmacy' and region == 'state'):
            response.extend(filters.pharmacy_college_by_state(i))
        elif(field == 'pharmacy' and region == 'city'):
            response.extend(filters.pharmacy_college_by_city(i))
        elif(field == 'nirf' and region == 'state'):
            response.extend(filters.nirf_colleges_by_state(i))
        elif(field == 'nirf' and region == 'city'):
            response.extend(filters.nirf_colleges_by_city(i))
    return response

# All Participating Institutes in NIRF (extracted json from https://www.nirfindia.org/2022/OverallRankingALL.html)


def paginate(data: array, page, limit):
    return data[(page-1)*limit:page*limit]


@app.get('/all', description="All NIRF colleges listed.")
async def allNirf(page: int = 1, limit: int = 50):
    try:
        async with aiofiles.open(os.path.join(os.getcwd(), "data", "nirfAllParticipatingColleges22.json")) as file:
            output = await file.read()
    except:
        raise HTTPException(status_code=503)

    return paginate(json.loads(output), page, limit)


# All Colleges Nirf Ranking
@app.get('/all/nirf')
async def allNirf(page: int = 1, limit: int = 50):
    try:
        async with aiofiles.open(os.path.join(os.getcwd(), "data", "nirfAllColleges.json")) as file:
            output = await file.read()
    except:
        raise HTTPException(status_code=503)

    return paginate(json.loads(output), page, limit)


@app.get('/all/nirf/state={state}')
async def allNirfByState(state: str or None = None):
    # multiple states will be seperated by '&' like Maharastra&Andhra Pradesh
    states_list = [x.strip() for x in state.split('&')]
    try:
        response = colleges_by_state_or_city(
            'nirf', 'state', states_list)
        if len(response) == 0:
            raise HTTPException(status_code=404, detail='State not found')
        return response
    except Exception as e:
        raise HTTPException(status_code=404, detail='State  not found')


@app.get('/all/nirf/city={city}')
async def allNirfByCity(city: str or None = None):
    city_list = [x.strip() for x in city.split('&')]
    try:
        response = colleges_by_state_or_city(
            'nirf', 'city', city_list)
        if len(response) == 0:
            raise HTTPException(status_code=404, detail='City not found')
        return response
    except Exception as e:
        raise HTTPException(status_code=404, detail='City  not found')


# Engineering Colleges
@app.get('/engineering_colleges')
async def engineeringColleges(page: int = 1, limit: int = 50):
    try:
        async with aiofiles.open(os.path.join(os.getcwd(), "data", "allEngineeringColleges.json")) as file:
            output = await file.read()
    except:
        raise HTTPException(status_code=404)
    return paginate(json.loads(output), page, limit)


@app.get('/engineering_colleges/nirf')
async def engineeringCollegesNirf(page: int = 1, limit: int = 50):
    try:
        async with aiofiles.open(os.path.join(os.getcwd(), "data", "nirfEngineeringColleges.json")) as file:
            output = await file.read()
    except:
        raise HTTPException(status_code=503)

    return paginate(json.loads(output), page, limit)


@app.get('/engineering_colleges/state={state}')
async def engineeringCollegesByState(state: str or None = None, page: int = 1, limit: int = 50):
    # multiple states will be seperated by '&' like Maharastra&Andhra Pradesh
    states_list = [x.strip() for x in state.split('&')]
    try:
        response = colleges_by_state_or_city(
            'engineering', 'state', states_list)
        if len(response) == 0:
            raise HTTPException(status_code=404, detail='State not found')
        return paginate(response, page, limit)
    except Exception as e:
        raise HTTPException(status_code=404, detail='State  not found')


@app.get('/engineering_colleges/city={city}')
async def engineeringCollegesByCity(city: str or None = None, page: int = 1, limit: int = 50):
    city_list = [x.strip() for x in city.split('&')]
    try:
        response = colleges_by_state_or_city('engineering', 'city', city_list)
        if len(response) == 0:
            raise HTTPException(status_code=404, detail='City not found')
        return paginate(response, page, limit)

    except Exception as e:
        raise HTTPException(status_code=404, detail='City not found')


# Medical Colleges
@app.get('/medical_colleges')
async def medicalColleges(page: int = 1, limit: int = 50):
    try:
        async with aiofiles.open(os.path.join(os.getcwd(), "data", "allMedicalColleges.json")) as file:
            output = await file.read()
    except:
        raise HTTPException(status_code=404)

    return paginate(json.loads(output), page, limit)


@app.get('/medical_colleges/nirf')
async def nirfMedicalColleges(page: int = 1, limit: int = 50):
    try:
        async with aiofiles.open(os.path.join(os.getcwd(), "data", "nirfMedicalColleges.json")) as file:
            output = await file.read()
    except:
        raise HTTPException(status_code=500)
    return paginate(json.loads(output), page, limit)


@app.get('/medical_colleges/state={state}')
def medicalCollegesByState(state: str or None = None, page: int = 1, limit: int = 50):
    # multiple states will be seperated by '&' like Maharastra&Andhra Pradesh
    states_list = [x.strip() for x in state.split('&')]
    try:
        response = colleges_by_state_or_city('medical', 'state', states_list)
        if len(response) == 0:
            raise HTTPException(status_code=404, detail='State not found')
        return paginate(response, page, limit)

    except Exception as e:
        raise HTTPException(
            status_code=404, detail='Some error occured, please try again')


@app.get('/medical_colleges/city={city}')
async def medicalCollegesByCity(city: str or None = None, page: int = 1, limit: int = 50):
    city_list = [x.strip() for x in city.split('&')]
    try:
        response = colleges_by_state_or_city('medical', 'city', city_list)
        if len(response) == 0:
            raise HTTPException(status_code=404, detail='City not found')
        return paginate(response, page, limit)

    except Exception as e:

        raise HTTPException(
            status_code=404, detail='Some error occured, please try again')


# Management Colleges
@app.get('/management_colleges')
async def managementColleges(page: int = 1, limit: int = 50):
    try:
        async with aiofiles.open(os.path.join(os.getcwd(), "data", "allManagementColleges.json")) as file:
            output = await file.read()
    except:
        raise HTTPException(status_code=404)
    return paginate(json.loads(output), page, limit)


@app.get('/management_colleges/nirf')
def managementCollegesNirf(page: int = 1, limit: int = 50):

    try:
        with open(os.path.join(os.getcwd(), "data", "nirfManagementColleges.json")) as file:
            output = json.load(file)
    except:
        raise HTTPException(status_code=503)

    return paginate(output, page, limit)


@app.get('/management_colleges/city={city}')
async def managementCollegesByCity(city: str or None = None, page: int = 1, limit: int = 50):
    city_list = [x.strip() for x in city.split('&')]
    try:
        response = colleges_by_state_or_city('management', 'city', city_list)
        if len(response) == 0:
            raise HTTPException(status_code=404, detail='City not found')
        return paginate(response, page, limit)
    except Exception as e:
        raise HTTPException(
            status_code=404, detail='Some error occured, please try again')


@app.get('/management_colleges/state={state}')
async def managementCollegesByState(state: str or None = None, page: int = 1, limit: int = 50):
    states_list = [x.strip() for x in state.split('&')]
    try:
        response = colleges_by_state_or_city(
            'management', 'state', states_list)
        if len(response) == 0:
            raise HTTPException(status_code=404, detail='State not found')
        return paginate(response, page, limit)

    except Exception as e:
        raise HTTPException(
            status_code=404, detail='Some error occured, please try again')


# Colleges
@app.get('/colleges')
async def allColleges(page: int = 1, limit: int = 50):
    try:
        async with aiofiles.open(os.path.join(os.getcwd(), "data", "allNirfColleges.json")) as file:
            output = await file.read()
    except:
        raise HTTPException(status_code=404)
    return paginate(json.loads(output), page, limit)


@app.get('/colleges/nirf')
async def nirfCollegesRanked(page: int = 1, limit: int = 50):
    try:
        async with aiofiles.open(os.path.join(os.getcwd(), "data", "nirfCollegesRanked.json")) as file:
            output = await file.read()
    except:
        raise HTTPException(status_code=404)
    return paginate(json.loads(output), page, limit)


# Pharmacy Colleges
@app.get('/pharmacy_colleges')
async def allParticipatingPharmacyCollege(page: int = 1, limit: int = 50):
    try:
        async with aiofiles.open(os.path.join(os.getcwd(), "data", "allParticipatingPharmacyCollege.json")) as file:
            output = await file.read()
    except:
        raise HTTPException(status_code=404)
    return paginate(json.loads(output), page, limit)


@app.get('/pharmacy_colleges/nirf')
async def pharmacyCollegesNirf(page: int = 1, limit: int = 50):
    try:
        async with aiofiles.open(os.path.join(os.getcwd(), "data", "nirfPharmacyColleges.json")) as file:
            output = await file.read()
    except:
        raise HTTPException(status_code=404)
    return paginate(json.loads(output), page, limit)


@app.get('/pharmacy_colleges/state={state}')
async def pharmacyCollegesByState(state: str or None = None, page: int = 1, limit: int = 50):
    # multiple states will be seperated by '&' like Maharastra&Andhra Pradesh
    states_list = [x.strip() for x in state.split('&')]
    try:
        response = colleges_by_state_or_city(
            'pharmacy', 'state', states_list)
        if len(response) == 0:
            raise HTTPException(status_code=404, detail='State not found')
        return paginate(response, page, limit)
    except Exception as e:
        raise HTTPException(status_code=404, detail='State  not found')


@app.get('/pharmacy_colleges/city={city}')
async def pharmacyCollegesByCity(city: str or None = None, page: int = 1, limit: int = 50):
    city_list = [x.strip() for x in city.split('&')]
    try:
        response = colleges_by_state_or_city(
            'pharmacy', 'city', city_list)
        if len(response) == 0:
            raise HTTPException(status_code=404, detail='City not found')
        return paginate(response, page, limit)
    except Exception as e:
        raise HTTPException(status_code=404, detail='City  not found')


# Dental Colleges

@app.get("/dental_colleges")
async def participating_dental_colleges(page: int = 1, limit: int = 50):
    try:
        async with aiofiles.open(os.path.join(os.getcwd(), "data", "allParticipatingDentalColleges.json")) as file:
            output = await file.read()
    except:
        raise HTTPException(status_code=404)
    return paginate(json.loads(output), page, limit)


@app.get('/dental_colleges/nirf')
async def nirf_dental_colleges(page: int = 1, limit: int = 50):
    try:
        async with aiofiles.open(os.path.join(os.getcwd(), "data", "nirfDentalColleges.json")) as file:
            output = await file.read()
    except:
        raise HTTPException(status_code=404)
    return paginate(json.loads(output), page, limit)


@app.get('/dental_colleges/state={state}')
async def dentalCollegesByState(state: str or None = None, page: int = 1, limit: int = 50):
    # multiple states will be seperated by '&' like Maharastra&Andhra Pradesh
    states_list = [x.strip() for x in state.split('&')]
    try:
        response = colleges_by_state_or_city(
            'dental', 'state', states_list)
        if len(response) == 0:
            raise HTTPException(status_code=404, detail='State not found')
        return paginate(response, page, limit)
    except Exception as e:
        raise HTTPException(status_code=404, detail='State  not found')


@app.get('/dental_colleges/city={city}')
async def dentalCollegesByCity(city: str or None = None, page: int = 1, limit: int = 50):
    # multiple states will be seperated by '&' like Maharastra&Andhra Pradesh
    cities_list = [x.strip() for x in city.split('&')]
    try:
        response = colleges_by_state_or_city(
            'dental', 'city', cities_list)
        if len(response) == 0:
            raise HTTPException(status_code=404, detail='City not found')
        return paginate(response, page, limit)
    except Exception as e:
        raise HTTPException(status_code=404, detail='City  not found')


# Law Colleges
@app.get('/law_colleges/nirf')
async def nirf_law_colleges(page: int = 1, limit: int = 50):
    try:
        async with aiofiles.open(os.path.join(os.getcwd(), "data", "nirfLawCollegesRanked.json")) as file:
            output = await file.read()
    except:
        raise HTTPException(status_code=404)
    return paginate(json.loads(output), page, limit)


# Architecture Colleges
@app.get('/architecture_colleges')
async def researchColleges(page: int = 1, limit: int = 50):
    try:
        async with aiofiles.open(os.path.join(os.getcwd(), "data", "allArchitectureColleges.json")) as file:
            output = await file.read()
    except:
        raise HTTPException(status_code=404)
    return paginate(json.loads(output), page, limit)


@app.get('/architecture_colleges/nirf')
async def architectureCollegesNirf(page: int = 1, limit: int = 50):
    try:
        async with aiofiles.open(os.path.join(os.getcwd(), "data", "nirfArchitectureColleges.json")) as file:
            output = await file.read()
    except:
        raise HTTPException(status_code=404)
    return paginate(json.loads(output), page, limit)


@app.get('/architecture_colleges/state={state}')
def architectureCollegesByState(state: str or None = None, page: int = 1, limit: int = 50):
    # multiple states will be seperated by '&' like Maharastra&Andhra Pradesh
    states_list = [x.strip() for x in state.split('&')]
    try:
        response = colleges_by_state_or_city(
            'architecture', 'state', states_list)
        if len(response) == 0:
            raise HTTPException(status_code=404, detail='State not found')
        return paginate(response, page, limit)

    except Exception as e:
        raise HTTPException(
            status_code=404, detail='Some error occured, please try again')


@app.get('/architecture_colleges/city={city}')
async def architectureCollegesByCity(city: str or None = None, page: int = 1, limit: int = 50):
    city_list = [x.strip() for x in city.split('&')]
    try:
        response = colleges_by_state_or_city('architecture', 'city', city_list)
        if len(response) == 0:
            raise HTTPException(status_code=404, detail='City not found')
        return paginate(response, page, limit)

    except Exception as e:

        raise HTTPException(
            status_code=404, detail='Some error occured, please try again')


# Research Colleges
@app.get('/research_colleges')
async def researchColleges(page: int = 1, limit: int = 50):
    try:
        async with aiofiles.open(r'data\allResearchColleges.json', 'r') as file:
            output = await file.read()
    except:
        raise HTTPException(status_code=404)
    return paginate(json.loads(output), page, limit)


@app.get('/research_colleges/nirf')
async def nirfResearchColleges(page: int = 1, limit: int = 50):
    try:
        async with aiofiles.open(os.path.join(os.getcwd(), "data", "nirfResearchColleges.json")) as file:
            output = await file.read()
    except:
        raise HTTPException(status_code=404)
    return paginate(json.loads(output), page, limit)


@app.get('/research_colleges/state={state}')
def researchCollegesByState(state: str or None = None, page: int = 1, limit: int = 50):
    # multiple states will be seperated by '&' like Maharastra&Andhra Pradesh
    states_list = [x.strip() for x in state.split('&')]
    try:
        response = colleges_by_state_or_city('research', 'state', states_list)
        if len(response) == 0:
            raise HTTPException(status_code=404, detail='State not found')
        return paginate(response, page, limit)

    except Exception as e:
        raise HTTPException(
            status_code=404, detail='Some error occured, please try again')


@app.get('/research_colleges/city={city}')
async def researchCollegesByCity(city: str or None = None, page: int = 1, limit: int = 50):
    city_list = [x.strip() for x in city.split('&')]
    try:
        response = colleges_by_state_or_city('research', 'city', city_list)
        if len(response) == 0:
            raise HTTPException(status_code=404, detail='City not found')
        return paginate(response, page, limit)

    except Exception as e:

        raise HTTPException(
            status_code=404, detail='Some error occured, please try again')


# University Endpoints
@app.get('/universities')
async def universities(page: int = 1, limit: int = 50):
    try:
        async with aiofiles.open(r'data/nirfUniversities.json', 'r') as file:
            output = await file.read()
    except:
        raise HTTPException(status_code=404)
    return paginate(json.loads(output), page, limit)


@app.get('/universities/city={city}')
def universitiesByCity(city, page: int = 1, limit: int = 50):
    city_list = [x.strip() for x in city.split('&')]
    try:
        response = []
        for i in city_list:
            i = i.replace(" ", "").lower()
            response.append(filters.univerities_by_city(i))

        if len(response) == 0:
            raise HTTPException(status_code=404, detail='City not found')
        return paginate(response, page, limit)

    except Exception as e:
        raise HTTPException(
            status_code=404, detail='Some error occured, please try again')


@app.get('/universities/state={state}')
def universitiesbyState(state, page: int = 1, limit: int = 50):
    states_list = [x.strip() for x in state.split('&')]
    try:
        response = []
        for i in states_list:
            i = i.replace(" ", "").lower()
            response.append(filters.univerities_by_state(i))

        if len(response) == 0:
            raise HTTPException(status_code=404, detail='State not found')
        return paginate(response, page, limit)

    except Exception as e:
        raise HTTPException(
            status_code=404, detail='Some error occured, please try again')


@app.get('/law_colleges/nirf')
async def nirfRankedLawColleges(page: int = 1, limit: int = 50):
    try:
        async with aiofiles.open(r'data/nirfLawCollegesRanked.json', 'r') as file:
            output = await file.read()
    except:
        raise HTTPException(status_code=404)
    return paginate(json.loads(output), page, limit)
