import pandas as pd
import json

scrapper = pd.read_html(
    'https://collegedunia.com/bsc-agriculture-colleges')

df = scrapper[0]

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

# collegesList
json_file = json.dumps(collegesList, indent=4)
with open('../data/allAgriculture.json', 'a') as file:
    file.write(json_file)
