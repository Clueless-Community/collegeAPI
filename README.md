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
