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

#Part 1 with console output
printDict(peopleData, ['first_name', 'last_name', 'email_address', 'title'])

#Part 2
dictLetterFreq = dict()

for person in peopleData:
    for cha in person['email_address']:
        if cha in dictLetterFreq:
            dictLetterFreq[cha] += 1
        else:
            dictLetterFreq[cha] = 1
            

          
