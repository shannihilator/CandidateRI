import os
import requests

authKey = os.environ['KEY']

#Make a get request to SalesLoft people data and return the json contents
def getPeopleData():
    urlApiPeople = "https://api.salesloft.com/v2/people.json"
    headers = {
        'Authorization' : 'Bearer ' + authKey
    }

    apiRequest = requests.get(urlApiPeople, headers = headers  )
    data = apiRequest.json()
    return data

#Temporary function for printing out the data; will be replaced by a function 
#in the SalesLoftGui Class
def printDict(dictData, colNames):
    for item in dictData:
        for col in colNames:
            print(item[col], end = ' ')
        print()
            

jsonPeopleData = getPeopleData()
peopleData = jsonPeopleData['data']
printDict(peopleData, ['first_name', 'last_name', 'email_address', 'title'])

          
