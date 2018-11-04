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
def printDict(listData, columns):
    for item in listData:
        for col in columns:
            print(item[col], end = ' ')
        print()
            

jsonPeopleData = getPeopleData()
peopleData = jsonPeopleData['data']

#Part 1 with console output
printDict(peopleData, ['first_name', 'last_name', 'email_address', 'title'])

#Part 2

def getPeopleLetterFreq(column):
    dictLetterFreq = dict()
    
    for person in peopleData:
        for cha in person[column]:
            if cha in dictLetterFreq:
                dictLetterFreq[cha] += 1
            else:
                dictLetterFreq[cha] = 1
    listLetterFreq = list(dictLetterFreq.items()) #Convert the dict to a list
    listLetterFreq.sort(key=itemgetter(1),reverse=True) #Sort items by frequency
    return listLetterFreq
        
def onclickFreqButton():
    listLetterFreq = getPeopleLetterFreq('email_address')
    guiSalesLoft.addTable(listLetterFreq, [0,1], ['Letter', 'Frequency'])
        
#GUI Code          
root = Tk()
guiSalesLoft = SalesLoftGUI(root)
guiSalesLoft.addTable(peopleData, ['first_name', 'last_name', 'email_address', 'title'],
                ['First Name','Last Name', 'Email', 'Job Title'])
                


guiSalesLoft.addButton("Letter Frequency (Emails)", onclickFreqButton)
root.mainloop()