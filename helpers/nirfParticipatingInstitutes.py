import pandas as pd
import json


url = "https://www.nirfindia.org/2022/OverallRankingALL.html"

df = pd.read_html(url)
result = df[0].to_json(orient='records')
parsed = json.loads(result)
all_participating_institutes = json.dumps(parsed, indent=4)

with open("../data/nirfAllParticipatingColleges22.json", "w") as f:
    f.write(all_participating_institutes))
    f.close()
