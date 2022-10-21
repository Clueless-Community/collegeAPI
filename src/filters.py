# Imports
import json
import os


# Engineering Colleges Filter
def processing(data, searchfor, present):
    output = []
    for i in range(len(data)):
        stateCheck = data[i][searchfor].replace(" ", '').lower()
        if stateCheck == present:
            output.append(data[i])
    return output


def engineering_colleges_by_state(state):

    with open(os.path.join(os.getcwd(), "data", "allEngineeringColleges.json")) as file:
        data = json.load(file)

    return processing(data, 'state', state)


def engineering_colleges_by_city(city):

    with open(os.path.join(os.getcwd(), "data", "allEngineeringColleges.json")) as file:
        data = json.load(file)
    return processing(data, 'city', city)


# Medical Colleges Filter
def medical_colleges_by_state(state):

    with open(os.path.join(os.getcwd(), "data", "allMedicalColleges.json")) as file:
        data = json.load(file)
    return processing(data, 'state', state)


def medical_colleges_by_city(city):

    with open(os.path.join(os.getcwd(), "data", "allMedicalColleges.json")) as file:
        data = json.load(file)
    return processing(data, 'city', city)


# Management Colleges Filter
def management_colleges_by_state(state):

    with open(os.path.join(os.getcwd(), "data", "allManagementColleges.json")) as file:
        data = json.load(file)
    return processing(data, 'State', state)


def management_colleges_by_city(city):

    with open(os.path.join(os.getcwd(), "data", "allManagementColleges.json")) as file:
        data = json.load(file)
    return processing(data, 'City', city)


# Research Colleges Filter
def research_colleges_by_state(state):

    with open(r'data\allResearchColleges.json', 'r') as file:
        data = json.load(file)
    return processing(data, 'state', state)


def research_colleges_by_city(city):

    with open(r'data\allResearchColleges.json', 'r') as file:
        data = json.load(file)

    return processing(data, 'city', city)


# University Filter
def univerities_by_city(city):

    with open("data/allUniversity.json", 'r') as file:
        data = json.load(file)
    output = []
    for i in range(len(data)):
        cityCheck = data[i]['city'].lower()
        if cityCheck == city:
            output.append(data[i])

    return output


def univerities_by_state(state):
    with open("data/allUniversity.json", 'r') as file:
        data = json.load(file)
    return processing(data, 'state', state)


# Architecture Colleges Filter
def architecture_colleges_by_state(state):

    with open(r'data\allArchitectureColleges.json', 'r') as file:
        data = json.load(file)
    return processing(data, 'state', state)


def architecture_colleges_by_city(city):

    with open(r'data\allArchitectureColleges.json', 'r') as file:
        data = json.load(file)
    return processing(data, 'city', city)


def dental_colleges_by_state(state):
    with open(r'data\nirfDentalColleges.json', 'r') as file:
        data = json.load(file)
    return processing(data, 'state', state)


def dental_colleges_by_city(city):
    with open(r'data\nirfDentalColleges.json', 'r') as file:
        data = json.load(file)
    return processing(data, 'city', city)
    return processing(data, 'city', city)


# filter phamarcy colleges by state
def pharmacy_college_by_state(state):
    with open(os.path.join(os.getcwd(), "data", "allParticipatingPharmacyCollege.json")) as file:
        data = json.load(file)
    return processing(data, 'state', state)


# filter phamarcy colleges by city
def pharmacy_college_by_city(city):
    with open(os.path.join(os.getcwd(), "data", "allParticipatingPharmacyCollege.json")) as file:
        data = json.load(file)
    return processing(data, 'city', city)


# filter all Nirf colleges
def nirf_colleges_by_state(state):
    with open(os.path.join(os.getcwd(), "data", "allNirfColleges.json")) as file:
        data = json.load(file)
    return processing(data, 'state', state)


def nirf_colleges_by_state(city):
    with open(os.path.join(os.getcwd(), "data", "allNirfColleges.json")) as file:
        data = json.load(file)
    return processing(data, 'city', city)
