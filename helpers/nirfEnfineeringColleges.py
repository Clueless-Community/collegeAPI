# Scrape the colleges listed in NIRF rankings only

import pandas as pd
import json

# First 200 Engineering Colleges
scrapper = pd.read_html(
    'https://www.nirfindia.org/2022/EngineeringRanking.html'
)
df1 = scrapper[0]
df1 = df1.drop(columns=['Institute ID', 'Score'], axis=1)


# For college in band 201-250
scrapper2 = pd.read_html(
    'https://www.nirfindia.org/2022/EngineeringRanking150.html'
)
rank_col1 = list(range(201,251))
df2 = scrapper2[0]
df2['Rank'] = rank_col1


# For 251-300
scrapper3 = pd.read_html(
    'https://www.nirfindia.org/2022/EngineeringRanking200.html'
)

rank_col3 = list(range(251,301))
df3 = scrapper3[0]
df3['Rank'] = rank_col3



# Concatinating the DataFrames
dfList = [df1, df2, df3]
dataFrame = pd.concat(dfList)
dataFrame

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
for i in range(len(dataFrame)):
    testList = dataFrame.iloc[i:, :].values
    testList2 = testList.tolist()
    name = nameSlice(testList2[0][0])
    testList2[0][0] = name
    testDict = convert_to_dict(testList2[0])
    collegesList.append(testDict)


json_file = json.dumps(collegesList, indent=4)
# print(json_file)
with open(r'data/nirfEngineeringColleges.json', 'w') as file:
    file.write(json_file)

    