# Project setup


## Fork and clone the repository
```bash
git clone https://github.com/nikhil25803/collegeAPI.git
```

## Change the directory
```bash
cd collegeAPI
```

## Activate the virtual environment
> For windows
```bash
env\Scripts\Activate.ps1
```
> For Linux
```bash
source env/scripts/activate
```

## Install the dependencies
```powershell
pip install -r requirements.txt
```

## Run the FastAPI server
```powershell
uvicorn main:app --reload
```

## Endpoints

**GET** `/engineeringColleges` 

This endpoint will return the list of all the engineering colleges in India with their city and state mentioned in JSON format as the output as shown :


```js
[
    {
        "name": "A G Patil Institute of Technology",
        "city": "Solapur",
        "state": "Maharashtra"
    },
    {
        "name": "A P Shah Institute Of Technology",
        "city": "Thane",
        "state": "Maharashtra"
    },
    ...
]
```


**GET** `/engineeringColleges/nirf`

This  will return a list of all the engineering colleges listed in NIRF in JSON format as an otput.

```js
[
    {
        "name": "Indian Institute of Technology Madras",
        "city": "Chennai",
        "state": "Tamil Nadu",
        "nirfRank": 1
    },
    {
        "name": "Indian Institute of Technology, Delhi",
        "city": "New Delhi",
        "state": "Delhi",
        "nirfRank": 2
    },
    ...
] 
```

**GET** `/engineeringColleges/nirf/city={name_of_the_city}` 

Pass the name of the city in the url, for example `/engineeringColleges/nirf/city=kolkata`

This will return the colleges in Kolkata as an output.

```js
[
    {
        "name": "Jadavpur University",
        "city": "Kolkata",
        "state": "West Bengal",
        "nirfRank": 11
    },
    {
        "name": "Heritage Institute of Technology",
        "city": "Kolkata",
        "state": "West Bengal",
        "nirfRank": 215
    },
    ...
]
```

**GET** `/engineeringColleges/nirf/state={name_of_the_state}`

Pass the name of the city in the url, for example `/engineeringColleges/nirf/state=westbengal`

This will return the colleges in West Bengal as an output.

```js
[
    {
        "name": "Indian Institute of Technology, Kharagpur",
        "city": "Kharagpur",
        "state": "West Bengal",
        "nirfRank": 5
    },
    {
        "name": "Jadavpur University",
        "city": "Kolkata",
        "state": "West Bengal",
        "nirfRank": 11
    },
    ...
]
```
