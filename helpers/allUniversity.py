import requests
import json
from bs4 import BeautifulSoup

URL = "https://www.nirfindia.org/2022/UniversityRanking.html"
r = requests.get(URL)

# If this line causes an error, run 'pip install html5lib' or install html5lib
soup = BeautifulSoup(r.content, 'html.parser')

colleges = []


td = soup.find_all("td")
for i in range(1, 1091, 11):
    college = dict()
    college["name"] = td[i].contents[0].string
    college["city"] = td[i+6].contents[0].string
    college["state"] = td[i+7].contents[0].string
    college["rank"] = td[i+9].contents[0].string
    colleges.append(college)


with open("../data/allUniversity.json", "w") as outfile:
    json.dump(colleges, outfile)
