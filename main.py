import os
import json
import aiofiles
from pandas import array
from src import filters
from fastapi import FastAPI, HTTPException, Request
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded


# Initiating a FastAPI application

API_METADATA = {
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

app = FastAPI(**API_METADATA)

limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

# Homepage
@app.get('/', tags=['home'])
@limiter.limit("5/minute")
async def home(request: Request):

    return API_METADATA


# Filter Function
def filter_colleges(field, region, region_list):
    response = []
    for i in region_list:
        region_req = i.replace(" ", "").lower()
        response.extend(filters.get_colleges(field, region, region_req))
    return response


def paginate(data: array, page, limit):
    return data[(page-1)*limit:page*limit]


@app.get('/all', description="All NIRF listed colleges.")
@limiter.limit("5/minute")
async def allNirf(request: Request,page: int = 1, limit: int = 50):

    file_name = "college_participated.json"
    output = filters.get_field_data(file_name)
    if output==-1:
        raise HTTPException(status_code=503)

    return paginate(json.loads(output), page, limit)


# All Colleges Nirf Ranking
@app.get('/all/nirf', description='All NIRF listed colleges ranking', tags=['all_NIRF_colleges_ranking'])
@limiter.limit("5/minute")
async def allNirf(request: Request,page: int = 1, limit: int = 50):

    file_name = "college_ranking.json"
    output = filters.get_field_data(file_name)
    if output==-1:
        raise HTTPException(status_code=503)

    return paginate(json.loads(output), page, limit)


@app.get('/all/nirf/state={state}', description='Filter all NIRF listed colleges by state', tags=['all_NIRF_colleges_ranking'])
@limiter.limit("5/minute")
async def allNirfByState(request: Request,state: str or None = None):

    response = filters.get_response("nirf", state=state)
    if response==-1:
        raise HTTPException(status_code=404, detail='State not found')

    return response


@app.get('/all/nirf/city={city}', description='Filter all NIRF listed colleges by city', tags=['all_NIRF_colleges_ranking'])
@limiter.limit("5/minute")
async def allNirfByCity(request: Request,city: str or None = None):

    response = filters.get_response("nirf", city=city)
    if response==-1:
        raise HTTPException(status_code=404, detail='City not found')

    return response


# Engineering Colleges
@app.get('/engineering_colleges', description='All engineering colleges', tags=['engineering_colleges'])
@limiter.limit("5/minute")
async def engineeringColleges(request: Request,page: int = 1, limit: int = 50):

    file_name = "engineering_participated.json"
    output = filters.get_field_data(file_name)
    if output==-1:
        raise HTTPException(status_code=503)
    
    return paginate(json.loads(output), page, limit)


@app.get('/engineering_colleges/nirf', description='All NIRF listed engineering colleges', tags=['engineering_colleges'])
@limiter.limit("5/minute")
async def engineeringCollegesNirf(request: Request,page: int = 1, limit: int = 50):

    file_name = "engineering_ranking.json"
    output = filters.get_field_data(file_name)
    if output==-1:
        raise HTTPException(status_code=503)

    return paginate(json.loads(output), page, limit)


@app.get('/engineering_colleges/state={state}', description='Filter engineering colleges by state', tags=['engineering_colleges'])
@limiter.limit("5/minute")
async def engineeringCollegesByState(request: Request,state: str or None = None, page: int = 1, limit: int = 50):

    response = filters.get_response("engineering", state=state)
    if response==-1:
        raise HTTPException(status_code=404, detail='State not found')

    return paginate(response, page, limit)


@app.get('/engineering_colleges/city={city}', description='Filter engineering colleges by city', tags=['engineering_colleges'])
@limiter.limit("5/minute")
async def engineeringCollegesByCity(request: Request,city: str or None = None, page: int = 1, limit: int = 50):

    response = filters.get_response("engineering", city=city)
    if response==-1:
        raise HTTPException(status_code=404, detail='City not found')

    return paginate(response, page, limit)

# Medical Colleges
@app.get('/medical_colleges', description='All medical colleges', tags=['medical_colleges'])
@limiter.limit("5/minute")
async def medicalColleges(request: Request,page: int = 1, limit: int = 50):

    file_name = "medical_participated.json"
    output = filters.get_field_data(file_name)
    if output==-1:
        raise HTTPException(status_code=503)

    return paginate(json.loads(output), page, limit)


@app.get('/medical_colleges/nirf', description='All NIRF listed medical colleges', tags=['medical_colleges'])
@limiter.limit("5/minute")
async def nirfMedicalColleges(request: Request,page: int = 1, limit: int = 50):

    file_name = "medical_ranking.json"
    output = filters.get_field_data(file_name)
    if output==-1:
        raise HTTPException(status_code=503)

    return paginate(json.loads(output), page, limit)


@app.get('/medical_colleges/state={state}', description='Filter medical colleges by state', tags=['medical_colleges'])
@limiter.limit("5/minute")
async def medicalCollegesByState(request: Request,state: str or None = None, page: int = 1, limit: int = 50):

    response = filters.get_response("medical", state=state)
    if response==-1:
        raise HTTPException(status_code=404, detail='State not found')

    return paginate(response, page, limit)


@app.get('/medical_colleges/city={city}', description='Filter medical colleges by city', tags=['medical_colleges'])
@limiter.limit("5/minute")
async def medicalCollegesByCity(request: Request,city: str or None = None, page: int = 1, limit: int = 50):

    response = filters.get_response("medical", city=city)
    if response==-1:
        raise HTTPException(status_code=404, detail='City not found')

    return paginate(response, page, limit)


# Management Colleges
@app.get('/management_colleges', description='All management colleges', tags=['management_colleges'])
@limiter.limit("5/minute")
async def managementColleges(request: Request,page: int = 1, limit: int = 50):

    file_name = "management_participated.json"
    output = filters.get_field_data(file_name)
    if output==-1:
        raise HTTPException(status_code=503)

    return paginate(json.loads(output), page, limit)


@app.get('/management_colleges/nirf', description='All NIRF listed colleges', tags=['management_colleges'])
@limiter.limit("5/minute")
async def managementCollegesNirf(request: Request,page: int = 1, limit: int = 50):

    file_name = "management_ranking.json"
    output = filters.get_field_data(file_name)
    if output==-1:
        raise HTTPException(status_code=503)

    return paginate(output, page, limit)

@app.get('/management_colleges/state={state}', description='Filter management colleges by state', tags=['management_colleges'])
@limiter.limit("5/minute")
async def managementCollegesByState(request: Request,state: str or None = None, page: int = 1, limit: int = 50):

    response = filters.get_response("management", state=state)
    if response==-1:
        raise HTTPException(status_code=404, detail='City not found')

    return paginate(response, page, limit)


@app.get('/management_colleges/city={city}', description='Filter management colleges by city', tags=['management_colleges'])
@limiter.limit("5/minute")
async def managementCollegesByCity(request: Request,city: str or None = None, page: int = 1, limit: int = 50):

    response = filters.get_response("management", city=city)
    if response==-1:
        raise HTTPException(status_code=404, detail='City not found')

    return paginate(response, page, limit)


# Colleges
@app.get('/colleges', description='All colleges listed by NIRF', tags=['colleges'])
@limiter.limit("5/minute")
async def allColleges(request: Request,page: int = 1, limit: int = 50):
    
    file_name = "college_participated.json"
    output = filters.get_field_data(file_name)
    if output==-1:
        raise HTTPException(status_code=503)
    
    return paginate(json.loads(output), page, limit)


@app.get('/colleges/nirf', description='Ranking of all NIRF listed colleges', tags=['colleges'])
@limiter.limit("5/minute")
async def nirfCollegesRanked(request: Request,page: int = 1, limit: int = 50):

    file_name = "college_ranking.json"
    output = filters.get_field_data(file_name)
    if output==-1:
        raise HTTPException(status_code=503)

    return paginate(json.loads(output), page, limit)


@app.get('/colleges/state={state}', description='Filter all colleges by state', tags=['colleges'])
@limiter.limit("5/minute")
async def collegesByState(request: Request,state: str or None = None, page: int = 1, limit: int = 50):
    response = filters.get_response("nirf", state=state)
    if response==-1:
        raise HTTPException(status_code=404, detail='State not found')

    return paginate(response, page, limit)


@app.get('/colleges/city={city}', description='Filter all colleges by city', tags=['colleges'])
@limiter.limit("5/minute")
async def collegesByCity(request: Request,city: str or None = None, page: int = 1, limit: int = 50):
    response = filters.get_response("nirf", city=city)
    if response==-1:
        raise HTTPException(status_code=404, detail='City not found')

    return paginate(response, page, limit)


# Pharmacy Colleges
@app.get('/pharmacy_colleges', description='All pharmacy colleges', tags=['pharmacy_colleges'])
@limiter.limit("5/minute")
async def allParticipatedPharmacyCollege(request: Request,page: int = 1, limit: int = 50):

    file_name = "pharmacy_participated.json"
    output = filters.get_field_data(file_name)
    if output==-1:
        raise HTTPException(status_code=503)

    return paginate(json.loads(output), page, limit)


@app.get('/pharmacy_colleges/nirf', description='All NIRF listed pharmacy colleges', tags=['pharmacy_colleges'])
@limiter.limit("5/minute")
async def pharmacyCollegesNirf(request: Request,page: int = 1, limit: int = 50):

    file_name = "pharmacy_ranking.json"
    output = filters.get_field_data(file_name)
    if output==-1:
        raise HTTPException(status_code=503)

    return paginate(json.loads(output), page, limit)


@app.get('/pharmacy_colleges/state={state}', description='Filter all pharmacy colleges by state', tags=['pharmacy_colleges'])
@limiter.limit("5/minute")
async def pharmacyCollegesByState(request: Request,state: str or None = None, page: int = 1, limit: int = 50):

    response = filters.get_response("pharmacy", state=state)
    if response==-1:
        raise HTTPException(status_code=404, detail='State not found')

    return paginate(response, page, limit)


@app.get('/pharmacy_colleges/city={city}', description='Filter all pharmacy colleges by city', tags=['pharmacy_colleges'])
@limiter.limit("5/minute")
async def pharmacyCollegesByCity(request: Request,city: str or None = None, page: int = 1, limit: int = 50):
    response = filters.get_response("pharmacy", city=city)
    if response==-1:
        raise HTTPException(status_code=404, detail='City not found')

    return paginate(response, page, limit)


# Dental Colleges
@app.get("/dental_colleges", description='List all dental colleges', tags=['dental_colleges'])
@limiter.limit("5/minute")
async def participating_dental_colleges(request: Request,page: int = 1, limit: int = 50):

    file_name = "dental_participated.json"
    output = filters.get_field_data(file_name)
    if output==-1:
        raise HTTPException(status_code=503)

    return paginate(json.loads(output), page, limit)


@app.get('/dental_colleges/nirf', description='List all NIRF listed dental colleges', tags=['dental_colleges'])
@limiter.limit("5/minute")
async def nirf_dental_colleges(request: Request,page: int = 1, limit: int = 50):

    file_name = "dental_ranking.json"
    output = filters.get_field_data(file_name)
    if output==-1:
        raise HTTPException(status_code=503)

    return paginate(json.loads(output), page, limit)


@app.get('/dental_colleges/state={state}', description='Filter dental colleges by given state', tags=['dental_colleges'])
@limiter.limit("5/minute")
async def dentalCollegesByState(request: Request,state: str or None = None, page: int = 1, limit: int = 50):

    response = filters.get_response("dental", state=state)
    if response==-1:
        raise HTTPException(status_code=404, detail='State not found')

    return paginate(response, page, limit)


@app.get('/dental_colleges/city={city}', description='Filter dental colleges by given city', tags=['dental_colleges'])
@limiter.limit("5/minute")
async def dentalCollegesByCity(request: Request,city: str or None = None, page: int = 1, limit: int = 50):

    response = filters.get_response("dental", city=city)
    if response==-1:
        raise HTTPException(status_code=404, detail='City not found')

    return paginate(response, page, limit)


# Law Colleges
@app.get('/law_colleges/nirf', description='All NIRF listed law colleges', tags=['law_colleges'])
@limiter.limit("5/minute")
async def nirf_law_colleges(request: Request,page: int = 1, limit: int = 50):
    
    file_name = "law_ranking.json"
    output = filters.get_field_data(file_name)
    if output==-1:
        raise HTTPException(status_code=503)

    return paginate(json.loads(output), page, limit)


@app.get('/law_colleges', description='All the participated law instututes', tags=['law_colleges'])
@limiter.limit("5/minute")
async def law_colleges(request: Request,page: int = 1, limit: int = 50):
    
    file_name = "law_participated.json"
    output = filters.get_field_data(file_name)
    if output==-1:
        raise HTTPException(status_code=503)

    return paginate(json.loads(output), page, limit)


@app.get('/law_colleges/state={state}', description='Filter law colleges by given state', tags=['law_colleges'])
@limiter.limit("5/minute")
async def dentalCollegesByState(request: Request,state: str or None = None, page: int = 1, limit: int = 50):
    response = filters.get_response("law", state=state)
    if response==-1:
        raise HTTPException(status_code=404, detail='State not found')

    return paginate(response, page, limit)


@app.get('/law_colleges/city={city}', description='Filter law colleges by given city', tags=['law_colleges'])
@limiter.limit("5/minute")
async def dentalCollegesByCity(request: Request,city: str or None = None, page: int = 1, limit: int = 50):

    response = filters.get_response("law", city=city)
    if response==-1:
        raise HTTPException(status_code=404, detail='City not found')

    return paginate(response, page, limit)


# Architecture Colleges
@app.get('/architecture_colleges', description='List all architecture colleges', tags=['architecture_colleges'])
@limiter.limit("5/minute")
async def researchColleges(request: Request,page: int = 1, limit: int = 50):
    
    file_name = "architecture_participated.json"
    output = filters.get_field_data(file_name)
    if output==-1:
        raise HTTPException(status_code=503)

    return paginate(json.loads(output), page, limit)


@app.get('/architecture_colleges/nirf', description='All NIRF listed architecture colleges', tags=['architecture_colleges'])
@limiter.limit("5/minute")
async def architectureCollegesNirf(request: Request,page: int = 1, limit: int = 50):

    file_name = "architecture_ranking.json"
    output = filters.get_field_data(file_name)
    if output==-1:
        raise HTTPException(status_code=503)

    return paginate(json.loads(output), page, limit)


@app.get('/architecture_colleges/state={state}', description='Filter architecture colleges by state', tags=['architecture_colleges'])
@limiter.limit("5/minute")
async def architectureCollegesByState(request: Request,state: str or None = None, page: int = 1, limit: int = 50):

    response = filters.get_response("architecture", state=state)
    if response==-1:
        raise HTTPException(status_code=404, detail='State not found')

    return paginate(response, page, limit)


@app.get('/architecture_colleges/city={city}', description='Filter architecture colleges by city', tags=['architecture_colleges'])
@limiter.limit("5/minute")
async def architectureCollegesByCity(request: Request,city: str or None = None, page: int = 1, limit: int = 50):

    response = filters.get_response("architecture", city=city)
    if response==-1:
        raise HTTPException(status_code=404, detail='City not found')

    return paginate(response, page, limit)


# Research Colleges
@app.get('/research_colleges', description='All research colleges', tags=['research_colleges'])
@limiter.limit("5/minute")
async def researchColleges(request: Request,page: int = 1, limit: int = 50):
    
    file_name = "research_ranking.json"
    output = filters.get_field_data(file_name)
    if output==-1:
        raise HTTPException(status_code=503)

    return paginate(json.loads(output), page, limit)


@app.get('/research_colleges/nirf', description='All NIRF listed research colleges', tags=['research_colleges'])
@limiter.limit("5/minute")
async def nirfResearchColleges(request: Request,page: int = 1, limit: int = 50):
    file_name = "research_ranking.json"
    output = filters.get_field_data(file_name)
    if output==-1:
        raise HTTPException(status_code=503)

    return paginate(json.loads(output), page, limit)


@app.get('/research_colleges/state={state}', description='Filter research colleges by state', tags=['research_colleges'])
@limiter.limit("5/minute")
async def researchCollegesByState(request: Request,state: str or None = None, page: int = 1, limit: int = 50):

    response = filters.get_response("research", state=state)
    if response==-1:
        raise HTTPException(status_code=404, detail='State not found')

    return paginate(response, page, limit)


@app.get('/research_colleges/city={city}', description='Filter research colleges by city', tags=['research_colleges'])
@limiter.limit("5/minute")
async def researchCollegesByCity(request: Request,city: str or None = None, page: int = 1, limit: int = 50):

    response = filters.get_response("research", city=city)
    if response==-1:
        raise HTTPException(status_code=404, detail='City not found')

    return paginate(response, page, limit)


# University Endpoints
@app.get('/universities', description="List all NIRF universities", tags=['universities'])
@limiter.limit("5/minute")
async def universities(request: Request,page: int = 1, limit: int = 50):

    file_name = "university_ranking.json"
    output = filters.get_field_data(file_name)
    if output==-1:
        raise HTTPException(status_code=503)

    return paginate(json.loads(output), page, limit)


@app.get('/universities/state={state}', description="Filter universities by state.", tags=['universities'])
@limiter.limit("5/minute")
async def universitiesbyState(request: Request,state, page: int = 1, limit: int = 50):
    response = filters.get_response("universities", state=state)
    if response==-1:
        raise HTTPException(status_code=404, detail='State not found')

    return paginate(response, page, limit)


@app.get('/universities/city={city}', description='Filter universities by city', tags=['universities'])
@limiter.limit("5/minute")
async def universitiesByCity(request: Request,city, page: int = 1, limit: int = 50):
    response = filters.get_response("universities", city=city)
    if response==-1:
        raise HTTPException(status_code=404, detail='City not found')

    return paginate(response, page, limit)


