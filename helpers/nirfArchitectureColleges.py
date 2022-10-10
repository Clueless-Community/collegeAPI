# Scrape the colleges listed in NIRF rankings only
import pandas as pd
import json

# 30 architecture Colleges
scrapper = pd.read_html(
    'https://www.nirfindia.org/2022/ArchitectureRanking.html'
)
df1 = scrapper[0]
df1 = df1.drop(columns=['Institute ID', 'Score'], axis=1)


# Function to remove 'More Details |' from each string
def nameSlice(str):
    list = [s for s in str]
    new_list = list[:len(list)-14]
    new_str = "".join(new_list)
    return new_str


# Function to convert two lists into a Dictionary
def convert_to_dict(list):
    keysName = ['name', 'city', 'state', 'nirfRank']
    dictValue = dict(zip(keysName, list))
    return dictValue


# Returning the final dictionary
collegesList = []
for i in range(len(df1)):
    testList = df1.iloc[i:, :].values
    testList2 = testList.tolist()
    name = nameSlice(testList2[0][0])
    testList2[0][0] = name
    testDict = convert_to_dict(testList2[0])
    collegesList.append(testDict)


json_file = json.dumps(collegesList, indent=4)
# print(json_file)
with open(r'data/nirfArchitectureColleges.json', 'w') as file:
    file.write(json_file)
