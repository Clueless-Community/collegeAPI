# Imports
import json, os

# Engineering Colleges Filter
def engineering_colleges_by_state(state):

    with open(r'data\allEngineeringColleges.json', 'r') as file:
        data = json.load(file)

    output = []
    for i in range(len(data)):
        stateCheck = data[i]['state'].replace(" ", '').lower()
        if stateCheck == state:
            output.append(data[i])
    return output


def engineering_colleges_by_city(city):

    with open(r'data\allEngineeringColleges.json', 'r') as file:
        data = json.load(file)
    output = []
    for i in range(len(data)):
        cityCheck = data[i]['city'].replace(" ", "").lower()
        if cityCheck == city:
            output.append(data[i])
    return output
    

# Medical Colleges Filter
def medical_colleges_by_state(state):
    
    with open(r'data\allMedicalColleges.json', 'r') as file:
        data = json.load(file)
    output = []
    for i in range(len(data)):
        stateCheck = data[i]['state'].replace(" ", "").lower()
        if stateCheck == state:
            output.append(data[i])
    return output


def medical_colleges_by_city(city):
    
    with open(r'data\allMedicalColleges.json', 'r') as file:
        data = json.load(file)
    output = []
    for i in range(len(data)):
        cityCheck = data[i]['city'].replace(" ", "").lower()
        if cityCheck == city:
            output.append(data[i])
    return output

# Management Colleges Filter
def management_colleges_by_state(state):
    
    with open(r'data\allManagementColleges.json', 'r') as file:
        data = json.load(file)
    output = []
    for i in range(len(data)):
        stateCheck = data[i]['state'].replace(" ", "").lower()
        if stateCheck == state:
            output.append(data[i])
    return output


def management_colleges_by_city(city):
    
    with open(r'data\allManagementColleges.json', 'r') as file:
        data = json.load(file)
    output = []
    for i in range(len(data)):
        cityCheck = data[i]['city'].replace(" ", "").lower()
        if cityCheck == city:
            output.append(data[i])
    return output
    
