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

jsonPeopleData = getPeopleData()
