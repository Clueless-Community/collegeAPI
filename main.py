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
@app.get('/', tags=['home'])
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


@app.get('/all', description="All NIRF listed colleges.", tags=['all_NIRF_colleges'])
async def allNirf(page: int = 1, limit: int = 50):
    try:
        async with aiofiles.open(os.path.join(os.getcwd(), "data", "nirfAllParticipatingColleges22.json")) as file:
            output = await file.read()
    except:
        raise HTTPException(status_code=503)

    return paginate(json.loads(output), page, limit)


# All Colleges Nirf Ranking
@app.get('/all/nirf', description='All NIRF listed colleges ranking', tags=['all_NIRF_colleges_ranking'])
async def allNirf(page: int = 1, limit: int = 50):
    try:
        async with aiofiles.open(os.path.join(os.getcwd(), "data", "nirfAllColleges.json")) as file:
            output = await file.read()
    except:
        raise HTTPException(status_code=503)

    return paginate(json.loads(output), page, limit)


@app.get('/all/nirf/state={state}', description='Filter all NIRF listed colleges by state', tags=['all_NIRF_colleges_ranking'])
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


@app.get('/all/nirf/city={city}', description='Filter all NIRF listed colleges by city', tags=['all_NIRF_colleges_ranking'])
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
@app.get('/engineering_colleges', description='All engineering colleges', tags=['engineering_colleges'])
async def engineeringColleges(page: int = 1, limit: int = 50):
    try:
        async with aiofiles.open(os.path.join(os.getcwd(), "data", "allEngineeringColleges.json")) as file:
            output = await file.read()
    except:
        raise HTTPException(status_code=404)
    return paginate(json.loads(output), page, limit)


@app.get('/engineering_colleges/nirf', description='All NIRF listed engineering colleges', tags=['engineering_colleges'])
async def engineeringCollegesNirf(page: int = 1, limit: int = 50):
    try:
        async with aiofiles.open(os.path.join(os.getcwd(), "data", "nirfEngineeringColleges.json")) as file:
            output = await file.read()
    except:
        raise HTTPException(status_code=503)

    return paginate(json.loads(output), page, limit)


@app.get('/engineering_colleges/state={state}', description='Filter engineering colleges by state', tags=['engineering_colleges'])
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


@app.get('/engineering_colleges/city={city}', description='Filter engineering colleges by city', tags=['engineering_colleges'])
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
@app.get('/medical_colleges', description='All medical colleges', tags=['medical_colleges'])
async def medicalColleges(page: int = 1, limit: int = 50):
    try:
        async with aiofiles.open(os.path.join(os.getcwd(), "data", "allMedicalColleges.json")) as file:
            output = await file.read()
    except:
        raise HTTPException(status_code=404)

    return paginate(json.loads(output), page, limit)


@app.get('/medical_colleges/nirf', description='All NIRF listed medical colleges', tags=['medical_colleges'])
async def nirfMedicalColleges(page: int = 1, limit: int = 50):
    try:
        async with aiofiles.open(os.path.join(os.getcwd(), "data", "nirfMedicalColleges.json")) as file:
            output = await file.read()
    except:
        raise HTTPException(status_code=500)
    return paginate(json.loads(output), page, limit)


@app.get('/medical_colleges/state={state}', description='Filter medical colleges by state', tags=['medical_colleges'])
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


@app.get('/medical_colleges/city={city}', description='Filter medical colleges by city', tags=['medical_colleges'])
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
@app.get('/management_colleges', description='All management colleges', tags=['management_colleges'])
async def managementColleges(page: int = 1, limit: int = 50):
    try:
        async with aiofiles.open(os.path.join(os.getcwd(), "data", "allManagementColleges.json")) as file:
            output = await file.read()
    except:
        raise HTTPException(status_code=404)
    return paginate(json.loads(output), page, limit)


@app.get('/management_colleges/nirf', description='All NIRF listed colleges', tags=['management_colleges'])
def managementCollegesNirf(page: int = 1, limit: int = 50):

    try:
        with open(os.path.join(os.getcwd(), "data", "nirfManagementColleges.json")) as file:
            output = json.load(file)
    except:
        raise HTTPException(status_code=503)

    return paginate(output, page, limit)


@app.get('/management_colleges/city={city}', description='Filter management colleges by city', tags=['management_colleges'])
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


@app.get('/management_colleges/state={state}', description='Filter management colleges by state', tags=['management_colleges'])
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
@app.get('/colleges', description='All colleges listed by NIRF', tags=['colleges'])
async def allColleges(page: int = 1, limit: int = 50):
    try:
        async with aiofiles.open(os.path.join(os.getcwd(), "data", "allNirfColleges.json")) as file:
            output = await file.read()
    except:
        raise HTTPException(status_code=404)
    return paginate(json.loads(output), page, limit)


@app.get('/colleges/nirf', description='Ranking of all NIRF listed colleges', tags=['colleges'])
async def nirfCollegesRanked(page: int = 1, limit: int = 50):
    try:
        async with aiofiles.open(os.path.join(os.getcwd(), "data", "nirfCollegesRanked.json")) as file:
            output = await file.read()
    except:
        raise HTTPException(status_code=404)
    return paginate(json.loads(output), page, limit)

@app.get('/colleges/state={state}', description='Filter all colleges by state', tags=['colleges'])
async def collegesByState(state: str or None = None, page: int = 1, limit: int = 50):
    # multiple states will be seperated by '&' like Maharastra&Andhra Pradesh
    states_list = [x.strip() for x in state.split('&')]
    try:
        response = colleges_by_state_or_city(
            'nirf', 'state', states_list)
        if len(response) == 0:
            raise HTTPException(status_code=404, detail='State not found')
        return paginate(response, page, limit)
    except Exception as e:
        raise HTTPException(status_code=404, detail='State  not found')


@app.get('/colleges/city={city}', description='Filter all colleges by city', tags=['colleges'])
async def collegesByCity(city: str or None = None, page: int = 1, limit: int = 50):
    city_list = [x.strip() for x in city.split('&')]
    try:
        response = colleges_by_state_or_city(
            'nirf', 'city', city_list)
        if len(response) == 0:
            raise HTTPException(status_code=404, detail='City not found')
        return paginate(response, page, limit)
    except Exception as e:
        raise HTTPException(status_code=404, detail='City  not found')


# Pharmacy Colleges
@app.get('/pharmacy_colleges', description='All pharmacy colleges', tags=['pharmacy_colleges'])
async def allParticipatingPharmacyCollege(page: int = 1, limit: int = 50):
    try:
        async with aiofiles.open(os.path.join(os.getcwd(), "data", "allParticipatingPharmacyCollege.json")) as file:
            output = await file.read()
    except:
        raise HTTPException(status_code=404)
    return paginate(json.loads(output), page, limit)


@app.get('/pharmacy_colleges/nirf', description='All NIRF listed pharmacy colleges', tags=['pharmacy_colleges'])
async def pharmacyCollegesNirf(page: int = 1, limit: int = 50):
    try:
        async with aiofiles.open(os.path.join(os.getcwd(), "data", "nirfPharmacyColleges.json")) as file:
            output = await file.read()
    except:
        raise HTTPException(status_code=404)
    return paginate(json.loads(output), page, limit)


@app.get('/pharmacy_colleges/state={state}', description='Filter all pharmacy colleges by state', tags=['pharmacy_colleges'])
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


@app.get('/pharmacy_colleges/city={city}', description='Filter all pharmacy colleges by city', tags=['pharmacy_colleges'])
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

@app.get("/dental_colleges", description='List all dental colleges', tags=['dental_colleges'])
async def participating_dental_colleges(page: int = 1, limit: int = 50):
    try:
        async with aiofiles.open(os.path.join(os.getcwd(), "data", "allParticipatingDentalColleges.json")) as file:
            output = await file.read()
    except:
        raise HTTPException(status_code=404)
    return paginate(json.loads(output), page, limit)


@app.get('/dental_colleges/nirf', description='List all NIRF listed dental colleges', tags=['dental_colleges'])
async def nirf_dental_colleges(page: int = 1, limit: int = 50):
    try:
        async with aiofiles.open(os.path.join(os.getcwd(), "data", "nirfDentalColleges.json")) as file:
            output = await file.read()
    except:
        raise HTTPException(status_code=404)
    return paginate(json.loads(output), page, limit)


@app.get('/dental_colleges/state={state}', description='Filter dental colleges by given state', tags=['dental_colleges'])
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


@app.get('/dental_colleges/city={city}', description='Filter dental colleges by given city', tags=['dental_colleges'])
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
@app.get('/law_colleges/nirf', description='All NIRF listed law colleges', tags=['law_colleges'])
async def nirf_law_colleges(page: int = 1, limit: int = 50):
    try:
        async with aiofiles.open(os.path.join(os.getcwd(), "data", "nirfLawCollegesRanked.json")) as file:
            output = await file.read()
    except:
        raise HTTPException(status_code=404)
    return paginate(json.loads(output), page, limit)

@app.get('/law_colleges', description='All the participated law instututes', tags=['law_colleges'])
async def law_colleges(page: int = 1, limit: int = 50):
    try:
        async with aiofiles.open(os.path.join(os.getcwd(), "data", "allParticipatedLawColleges.json")) as file:
            output = await file.read()
    except:
        raise HTTPException(status_code=404)
    return paginate(json.loads(output), page, limit)


# Architecture Colleges
@app.get('/architecture_colleges', description='List all architecture colleges', tags=['architecture_colleges'])
async def researchColleges(page: int = 1, limit: int = 50):
    try:
        async with aiofiles.open(os.path.join(os.getcwd(), "data", "allArchitectureColleges.json")) as file:
            output = await file.read()
    except:
        raise HTTPException(status_code=404)
    return paginate(json.loads(output), page, limit)


@app.get('/architecture_colleges/nirf', description='All NIRF listed architecture colleges', tags=['architecture_colleges'])
async def architectureCollegesNirf(page: int = 1, limit: int = 50):
    try:
        async with aiofiles.open(os.path.join(os.getcwd(), "data", "nirfArchitectureColleges.json")) as file:
            output = await file.read()
    except:
        raise HTTPException(status_code=404)
    return paginate(json.loads(output), page, limit)


@app.get('/architecture_colleges/state={state}', description='Filter architecture colleges by state', tags=['architecture_colleges'])
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


@app.get('/architecture_colleges/city={city}', description='Filter architecture colleges by city', tags=['architecture_colleges'])
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
@app.get('/research_colleges', description='All research colleges', tags=['research_colleges'])
async def researchColleges(page: int = 1, limit: int = 50):
    try:
        async with aiofiles.open(r'data\allResearchColleges.json', 'r') as file:
            output = await file.read()
    except:
        raise HTTPException(status_code=404)
    return paginate(json.loads(output), page, limit)


@app.get('/research_colleges/nirf', description='All NIRF listed research colleges', tags=['research_colleges'])
async def nirfResearchColleges(page: int = 1, limit: int = 50):
    try:
        async with aiofiles.open(os.path.join(os.getcwd(), "data", "nirfResearchColleges.json")) as file:
            output = await file.read()
    except:
        raise HTTPException(status_code=404)
    return paginate(json.loads(output), page, limit)


@app.get('/research_colleges/state={state}', description='Filter research colleges by state', tags=['research_colleges'])
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


@app.get('/research_colleges/city={city}', description='Filter research colleges by city', tags=['research_colleges'])
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
@app.get('/universities', description="List all NIRF universities", tags=['universities'])
async def universities(page: int = 1, limit: int = 50):
    try:
        async with aiofiles.open(r'data/nirfUniversities.json', 'r') as file:
            output = await file.read()
    except:
        raise HTTPException(status_code=404)
    return paginate(json.loads(output), page, limit)


@app.get('/universities/city={city}', description='Filter universities by city', tags=['universities'])
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


@app.get('/universities/state={state}', description="Filter universities by state.", tags=['universities'])
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