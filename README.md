<h1 align=center> CollegeAPI </h1>

<h3 align=center> Ever faced a problem while collecting the data of Indian Colleges? Here we are with the solution, <b>College API</b>.<br>An API that helps you to fetch the data of Indian Colleges.⚡</h3>

----

<p align="center">
  <a href="https://github.com/Clueless-Community/collegeAPI/issues"><img src="https://img.shields.io/github/issues/Clueless-Community/collegeAPI.svg?style=for-the-badge&logo=appveyor" /></a>&nbsp;&nbsp;
  <a href="https://github.com/Clueless-Community/collegeAPI/fork"><img src="https://img.shields.io/github/forks/Clueless-Community/collegeAPI.svg?style=for-the-badge&logo=appveyor" /></a>&nbsp;&nbsp;
  <a href="#"><img src="https://img.shields.io/github/stars/Clueless-Community/collegeAPI.svg?style=for-the-badge&logo=appveyor" /></a>&nbsp;&nbsp;
  <a href="https://github.com/Clueless-Community/collegeAPI/blob/master/LICENSE"><img src="https://img.shields.io/github/license/Clueless-Community/collegeAPI.svg?style=for-the-badge&logo=appveyor" /></a>&nbsp;&nbsp;
</p>

---

## Tech Stack 💻

  ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
  ![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)

---


## What do we exactly do?
The ambition of this project is to provide data of Indian Colleges from all the categories listed in NIRF through different endpoints. We also enable the user to filter the college by the desired city and state.

## Wants to contribute?👀
You can contribute to this project under [Hacktoberfest 2022](https://hacktoberfest.com/) 🤩 

![image](https://user-images.githubusercontent.com/70385488/192114009-0830321a-d227-4a4d-8411-6c03b54d7ce6.png)

## How to contribute?🤔

We recommend you to go through the [CONTRIBUTING.md](https://github.com/Clueless-Community/collegeAPI/blob/main/CONTRIBUTING.md) where we have mentioned all the guidelines that help you to set up the project and make some awesome contributions 😄

---

## Endpoints

| Method   |      Path      |  Description |
|----------|:-------------:|------:|
| **GET** |  `/` | Gives a description of the API |
| **GET** |  `/all` | Fetch the list of all participating collges ranked by NIRF |
| **GET** |  `/all/nirf` | Fetch the list of overall colleges ranked by NIRF |
| **GET** |  `/all/nirf/state={state}` | Fetch the list of colleges ranked by NIRF in the state(s) passed by the user as a `parameter` |
| **GET** |  `/all/nirf/city={city}` | Fetch the list of colleges ranked by NIRF in the city(ies) passed by the user as a `parameter` |
| **GET** | `/engineering_colleges` | Fetch the list of all the engineering colleges in India. |
| **GET** |  `/engineering_colleges/nirf` | Fetch the list of all the 300 engineering colleges ranked by NIRF. In this endpoint, the rank of the colleges will be provided along with the other details. |
| **GET** |  `/engineering_colleges/state={state}` | Fetch the list of all the engineering colleges in the state passed by the user as a `parameter`. |
| **GET** |  `/engineering_colleges/city={city}` | Fetch the list of all the engineering colleges in the city passed by the user as a `parameter`.  |
| **GET** |  `/medical_colleges` | Fetch the list of all the medical colleges in India.  |
| **GET** |  `/medical_colleges/nirf` | Fetch the list of all the medical colleges ranked by NIRF. |
| **GET** |  `/medical_colleges/state={state}` | Fetch the list of all the medical colleges in the state passed by the user as a `parameter`.  |
| **GET** |  `/medical_colleges/city={city}` | Fetch the list of all the medical colleges in the city passed by the user as a `parameter`.  |
| **GET** |  `/management_colleges` | Fetch the list of all the management colleges in India.  |
| **GET** |  `/management_colleges/nirf` | Fetch the list of all the 300 management colleges ranked by NIRF. In this endpoint, the rank of the colleges will be provided along with the other details.  |
| **GET** |  `/management_colleges/state={state}` | Fetch the list of all the management colleges in the state passed by the user as a `parameter`.  |
| **GET** |  `/management_colleges/city={city}` | Fetch the list of all the management colleges in the city passed by the user as a `parameter`.  |
| **GET** |  `/colleges` | Fetch the list of all the colleges in India. |
| **GET** |  `/colleges/nirf` | Fetch the list of all the colleges ranked by NIRF.  |
| **GET** |  `/colleges/state={state}` | Fetch the list of colleges in the state passed by the user as a `parameter`.  |
| **GET** |  `/colleges/city={city}` | Fetch the list of colleges in the city passed by the user as a `parameter`.  |
| **GET** |  `/pharmacy_colleges` | Fetch the list of all the pharmacy colleges.  |
| **GET** |  `/pharmacy_colleges/nirf` | Fetch the list of all the pharmacy colleges listed in NIRF.  |
| **GET** |  `/pharmacy_colleges/state={state}` | Fetch the list of pharmacy colleges in the state passed by the user as a `parameter`.  |
| **GET** |  `/pharmacy_colleges/city={city}` | Fetch the list of pharmacy colleges in the city passed by the user as a `parameter`.  |
| **GET** |  `/dental_colleges` | Fetch the list of all the dental colleges in India.  |
| **GET** |  `/dental_colleges/nirf` | Fetch the list of dental colleges listed in NIRF.  |
| **GET** |  `/dental_colleges/state={state}` | Fetch the list of all the dental colleges in the state passed by the user as a `parameter`.  |
| **GET** |  `/dental_colleges/city={city}` | Fetch the list of all the dental colleges in the city passed by the user as a `parameter`.  |
| **GET** |  `/law_colleges/nirf` | Fetch the list of law colleges listed in NIRF.  |
| **GET** |  `/architecture_colleges` | Fetch the list of all architecture colleges.  |
| **GET** |  `/architecture_colleges/nirf` | Fetch the list of architecture colleges listed in NIRF.  |
| **GET** |  `/architecture_colleges/state={state}` | Fetch the list of all the architecture colleges in the state passed by the user as a `parameter`.  |
| **GET** |  `/architecture_colleges/city={city}` | Fetch the list of all the architecture colleges in the city passed by the user as a `parameter`.  |
| **GET** |  `/research_colleges` | Fetch the list of all research colleges.  |
| **GET** |  `/research_colleges/nirf` | Fetch the list of research colleges listed in NIRF.  |
| **GET** |  `/research_colleges/state={state}` | Fetch the list of all the research colleges in the state passed by the user as a `parameter`.  |
| **GET** |  `/research_colleges/city={city}` | Fetch the list of all the research colleges in the city passed by the user as a `parameter`.  |
| **GET** |  `/universities` | Fetch the list of all the universities in India.  |
| **GET** |  `/universities/state={state}` | Fetch the list of all the universities in the state passed by the user as a `parameter`.  |
| **GET** |  `/universities/city={city}` | Fetch the list of all the universities in the city passed by the user as a `parameter`.  |

----

> For pagination add page and limit as query params i.e. `/all/?page=1&limit=10`

<h2 align='center'> Project maintainers </h2>
<table align='center'>
<tr>
    <td align="center">
        <a href="https://github.com/nikhil25803">
            <img src="https://avatars.githubusercontent.com/u/93156825?v=4" width="100;" alt="Nikhil Raj"/>
            <br />
            <sub><b>Nikhil Raj</b></sub>
        </a>
    </td>
  </tr>
</table>

---