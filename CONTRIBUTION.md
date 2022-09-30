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