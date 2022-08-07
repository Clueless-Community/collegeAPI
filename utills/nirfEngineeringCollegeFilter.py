import pandas as pd

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
df= dataFrame

# List of Cities
cityList = df['City'].tolist()

# Removing Duplicates
final = [*set(cityList)]


# Removing 'More Details |' from some string
def nameSlice(str):
    list = [s for s in str]
    new_list = list[:len(list)-14]
    new_str = "".join(new_list)
    return new_str


# Convert into Dictionary
def convert_to_dict(list):
    keysName = ['name', 'city', 'state', 'nirfRank']
    dictValue = dict(zip(keysName, list))
    return dictValue



# Function to search by City
def searchByCity(name): 
    collegesList = []
    if name in final:
        ans = df[df['City'] == f"{name}"]
        
        for i in range(len(ans)):
            testList = ans.iloc[i:, :].values
            testList2 = testList.tolist()

            if '|' in testList2[0][0].split(' '):
                name = nameSlice(testList2[0][0])
                testList2[0][0] = name
            
            testDict = convert_to_dict(testList2[0])
            collegesList.append(testDict)   
    else:
        return {
            "Status":"City entered didn't match"
        }

    return collegesList


# For Colleges, extracing list of colleges
stateList = df['State'].tolist()
for i in range(len(stateList)):
    name = stateList[i]
    splits = name.split(' ')
    if len(splits) > 1:
        name = "".join(splits)
        stateList[i] = name.lower()
    else:
        stateList[i] = name.lower()

# Adding it as a new Column to avoid nameing convention conflicts (Note: Data Frame has now been updated)
df['NewState'] = stateList

def searchByState(name): 
    result = []
    if name in stateList:
        ans = df[df['NewState'] == f"{name}"]
        
        for i in range(len(ans)):
            testList = ans.iloc[i:, :].values
            testList2 = testList.tolist()

            if '|' in testList2[0][0].split(' '):
                name = nameSlice(testList2[0][0])
                testList2[0][0] = name
            
            testDict = convert_to_dict(testList2[0])
            result.append(testDict)   
    else:
        print("Error")

    return result