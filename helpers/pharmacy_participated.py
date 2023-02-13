# Participated Institutes: Pharmacy

import pandas as pd
import json

url = "https://www.nirfindia.org/2022/PharmacyRankingALL.html"

# Scraping the html document to load the tabular list of universities
df: pd.DataFrame = pd.read_html(url)[0][["Name", "City", "State"]]
df.columns = df.columns.str.lower()

result = df.to_json(orient="records")
parsed = json.loads(result)
pharmacy_participated = json.dumps(parsed, indent=4)

# Writing the json formatted data to a file
with open("./data/pharmacy_participated.json", "w") as f:
    f.write(pharmacy_participated)
    f.close()
