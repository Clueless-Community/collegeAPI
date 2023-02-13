# Ranking: Management

import pandas as pd
import json

url = "https://www.nirfindia.org/2022/ManagementRanking.html"

# Scraping the html document to load the tabular list of institutes
df: pd.DataFrame = pd.read_html(url)[0][["Name", "City", "Rank", "State"]]
df.columns = df.columns.str.lower()

# Removing "More Details |" from institute names
df['name'] = df['name'].str.replace('More Details |', '', regex=False)

result = df.to_json(orient="records")
parsed = json.loads(result)
management_ranking = json.dumps(parsed, indent=4)

# Writing the json formatted data to a file
with open("./data/management_ranking.json", "w") as f:
    f.write(management_ranking)
    f.close()
