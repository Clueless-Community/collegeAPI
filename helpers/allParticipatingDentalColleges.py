
import pandas as pd
import json

url = 'https://www.nirfindia.org/2022/DentalRankingALL.html'
df = pd.read_html(url)

# convert to json
result = df[0].to_json(orient='records')
parsed = json.loads(result)
all_dental_college = json.dumps(parsed, indent=4)

with open(r'../data/allParticipatingDentalCollege.json', 'w+') as file:
    file.write(all_dental_college)
