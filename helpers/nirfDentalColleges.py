import pandas as pd
import json
import os
from typing import List, Dict, Any

# Scraping the html document to load the tabular list of dental colleges
scrapper = pd.read_html("https://www.nirfindia.org/2022/DentalRanking.html")

df: pd.core.frame.DataFrame = scrapper[0]
df: pd.core.frame.DataFrame = df.drop(labels='Score', axis=1)
df['Name'] = df['Name'].str.replace('More Details |', '', regex=False)


formatted_df: pd.core.frame.DataFrame = df.iloc[:, 1:]
formatted_df_list: List = formatted_df.values.tolist()

# Function to convert a passed list to a dictionary with certain keynames


def convert_list_to_dict(l: List):
    keysName = ['name', 'city', 'state', 'nirfRank']
    dictValue = dict(zip(keysName, l))
    return dictValue


# List of nirf ranked dental colleges with name, city, state and rank
college_list: List = []

for item in formatted_df_list:
    item_dict: Dict[str, Any] = convert_list_to_dict(item)
    college_list.append(item_dict)

# Writing the json formatted data to a file
with open(os.path.join(os.pardir, "data", "nirfDentalColleges.json"), 'w') as fp:
    json.dump(college_list, fp)
