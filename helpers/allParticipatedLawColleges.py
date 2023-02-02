import pandas as pd
import json
import os
from typing import List, Dict, Any

# Scraping the html document to load the tabular list of participated law colleges
scrapper = pd.read_html("https://www.nirfindia.org/2022/LawRankingALL.html")

df: pd.core.frame.DataFrame = scrapper[0]
formatted_df: pd.core.frame.DataFrame = df.iloc[:, :]
formatted_df_list: List = formatted_df.values.tolist()

# Function to convert a passed list to a dictionary with certain keynames


def convert_list_to_dict(l: List):
    keysName = ['name', 'city', 'state']
    dictValue = dict(zip(keysName, l))
    return dictValue


college_list: List = []

for item in formatted_df_list:
    item_dict: Dict[str, Any] = convert_list_to_dict(item)
    college_list.append(item_dict)
#print(college_list)
# Writing the json formatted data to a file
with open(r'data\allParticipatedLawColleges.json', 'w') as fp:
    json.dump(college_list, fp)
