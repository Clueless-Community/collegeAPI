import json
from requests_html import HTMLSession

s= HTMLSession()

url = 'https://www.nirfindia.org/2022/ResearchRanking.html'

r = s.get(url)

table = r.html.find('table')[0]

'''for row in table.find('tr'):
    for c in row.find('td'):
        print(c.text)'''

tabledata = [[c.text for c in row.find('td')] for row in table.find('tr')]

tableheader = [[c.text for c in row.find('th')] for row in table.find('tr')][0]

res = [dict(zip(tableheader, t)) for t in tabledata]

with open('allMedicalColleges.json', 'w') as f:
    json.dump(res, f)