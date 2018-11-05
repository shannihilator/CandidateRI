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
def printList(listData, columns):
    for item in listData:
        for col in columns:
            print(item[col], end = '\t')
        print()
            

#Part 2

def getPeopleLetterFreq(column):
    #Use a dictionary to count the frequency of letters
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

#Part 3


def generateSimilarityList(strings, alpha=.9):
    similarityList = []
    for i in range(len(strings)):
        for j in range(i):
            similarity = getSimilarity(strings[i],strings[j])
            if similarity > alpha:
                similarityList.append([
                    strings[i], 
                    strings[j],
                    similarity
                    ]
                )
    return similarityList
            
#Returns the simillarity between two strings by counting common characters
def getSimilarity(str1, str2, ignoreCase = True):
    commonChars = 0
    maxStrLen = max(len(str1),len(str2))
    
    if ignoreCase:
        str1 = str1.lower()
        str2 = str2.lower()
        
    for c in str1:
        if str2.find(c) >= 0: #If the character was found
            str2.replace(c,'',1) #Remove it
            commonChars +=1
    return commonChars/maxStrLen

def getColumnFromTable(data, column):
    return [x[column] for x in data]

def onclickDuplicatesButton():
    listDuplicates = generateSimilarityList(getColumnFromTable(peopleData,'email_address'))
    guiSalesLoft.addTable(listDuplicates, [0,1,2], ['Email 1', 'Email 2', 'Similarity'])

#Get Data
jsonPeopleData = getPeopleData()
peopleData = jsonPeopleData['data']

        
#GUI Code          
root = Tk()
guiSalesLoft = SalesLoftGUI(root)
guiSalesLoft.addTable(peopleData, ['first_name', 'last_name', 'email_address', 'title'],
                ['First Name','Last Name', 'Email', 'Job Title'])
guiSalesLoft.addButton("Letter Frequency (Emails)", onclickFreqButton)
guiSalesLoft.addButton("Find Duplicates", onclickDuplicatesButton)
root.mainloop()