import pandas as pd
import json
# Scrape all the colleges participated in


scrapper = pd.read_html(
    'https://collegedunia.com/bsc-agriculture-colleges')

df = scrapper[0]
df = df.fillna(value="")

test = df.iloc[2:, :].values
testList = test.tolist()


def convert_to_dict(list):
    keysName = ['Name', 'City', 'State']
    dictValue = dict(zip(keysName, list))
    return dictValue


collegesList = []
for i in range(len(df)):
    testList = df.iloc[i:, :].values
    testList2 = testList.tolist()
    testDict = convert_to_dict(testList2[0])
    collegesList.append(testDict)
    # continue

# collegesList
json_file = json.dumps(collegesList, indent=4)
with open(r'data/allAgricultureColleges.json', 'w') as file:
    file.write(json_file)
