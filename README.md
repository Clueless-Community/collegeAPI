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
http://127.0.0.1:8000/engineeringColleges/nirf - This  will return a JSON file of all the 
engineering colleges listed in NIRF

Output :
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

`http://127.0.0.1:8000/engineeringColleges/nirf/city={name_of_the_city}` - Pass the name of the city in the url. 

For example http://127.0.0.1:8000/engineeringColleges/nirf/city=kolkata - This will return the colleges in Kolkata as the output

Output:
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

`http://127.0.0.1:8000/engineeringColleges/nirf/state={name_of_the_state}` - Pass the name of the city in the url. 

For example http://127.0.0.1:8000/engineeringColleges/nirf/state=westbengal - This will return the colleges in West Bengal as the output

Output :
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