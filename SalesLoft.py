import os
import requests
from SalesLoftGui import SalesLoftGUI
from tkinter import Tk
from operator import itemgetter

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
listLetterFreq = list(dictLetterFreq.items()) #Convert the dict to a list
listLetterFreq.sort(key=itemgetter(1),reverse=True) #Sort items by frequency
          
root = Tk()
my_gui = SalesLoftGUI(root)
my_gui.addTable(peopleData, ['first_name', 'last_name', 'email_address', 'title'],
                ['First Name','Last Name', 'Email', 'Job Title'])
                
my_gui.addTable(listLetterFreq, [0,1], ['Letter', 'Frequency'])
root.mainloop()