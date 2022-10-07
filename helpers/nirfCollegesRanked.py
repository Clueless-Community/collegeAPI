from pathlib import Path
import pandas as pd
import json

url_1 = "https://www.nirfindia.org/2022/CollegeRanking.html"
url_2 = "https://www.nirfindia.org/2022/CollegeRanking150.html"
url_3 = "https://www.nirfindia.org/2022/CollegeRanking200.html"

urls = [url_1, url_2, url_3]

df_page = []
for url in urls:
    df = pd.read_html(url)
    df_page.append(df[0])

df_1 = df_page[0].drop(['Institute ID', 'Score'], axis=1)
df_1['Name'] = df_1['Name'].str.replace('More Details |', '', regex=False)

df_page[1].insert(len(df_page[1].columns), 'Rank',
                  range(101, 101 + len(df_page[1])))
df_2 = df_page[1]

df_page[2].insert(len(df_page[2].columns), 'Rank',
                  range(151, 151 + len(df_page[2])))
df_3 = df_page[2]

dataFrame = pd.concat([df_1, df_2, df_3])

result = dataFrame.to_json(orient='records')
parsed = json.loads(result)
nirfRanked_list = json.dumps(parsed, indent=4)

with open(r'../data/nirfCollegesRanked.json', 'w+') as file:
    file.write(nirfRanked_list)
