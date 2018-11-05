import os
import requests
from SalesLoftGui import SalesLoftGUI
from tkinter import Tk
from operator import itemgetter

authKey = os.environ['KEY']

#Helper methods 

#Extracts a single column from a list of lists/tuples/dicts
def getColumnFromTable(data, column):
    return [x[column] for x in data]            

#Part 1

#Make a get request to a SalesLoft api and return the json contents
def getData(urlApi):
    headers = {
        'Authorization' : 'Bearer ' + authKey
    }

    apiRequest = requests.get(urlApi, headers = headers  )
    data = apiRequest.json()
    return data

#Part 2

#Returns the frequency of letters in a list of strings
def getLetterFreq(listStrings):
    #Use a dictionary to count the frequency of letters
    dictLetterFreq = dict()
    for string in listStrings:
        for cha in string:
            if cha in dictLetterFreq:
                dictLetterFreq[cha] += 1
            else:
                dictLetterFreq[cha] = 1
    listLetterFreq = list(dictLetterFreq.items()) #Convert the dict to a list
    listLetterFreq.sort(key=itemgetter(1),reverse=True) #Sort items by frequency
    return listLetterFreq

#Part 3

#Returns a list where each row is (string1, string2, similarity)
#Only strings where similarity > alpha in the list
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
    similarityList.sort(key=itemgetter(2),reverse=True) #Sort items by frequency
    return similarityList
            
#Returns the simillarity between two strings by counting common characters
#Obvious drawbacks such as "abc" and ""cba" having 1.0 similarity
#However, it should have a very few false negatives
#A better implementation would be to use a well know algorithm to compute
#a metric like the Levenshtein Distance
def getSimilarity(str1, str2, ignoreCase = True):
    commonChars = 0
    maxStrLen = max(len(str1),len(str2))
    
    if ignoreCase:
        str1 = str1.lower()
        str2 = str2.lower()
        
    for c in str1:

        if str2.find(c) >= 0: 
            str2.replace(c,'',1)  #Remove exactly one of it, so duplicate 
                            #characters are corretly handled
            commonChars +=1
    return commonChars/maxStrLen

#Event Handlers

#Handles the event when the "Letter Frequency" button is pressed        
def onclickFreqButton():
    listEmails = getColumnFromTable(peopleData, 'email_address')
    listLetterFreq = getLetterFreq(listEmails)
    guiSalesLoft.addTable(listLetterFreq, [0,1], ['Letter', 'Frequency'])

#Handles the event when the "Find Duplicates" button is pressed
def onclickDuplicatesButton():
    listEmails = getColumnFromTable(peopleData,'email_address')
    listDuplicates = generateSimilarityList(listEmails,.7)
    guiSalesLoft.addTable(listDuplicates, [0,1,2], ['Email 1', 'Email 2', 'Similarity'])

#Program execution starts here

#Get Data
peopleData = getData('https://api.salesloft.com/v2/people.json')['data']

        
#GUI Code          
root = Tk()
guiSalesLoft = SalesLoftGUI(root)
guiSalesLoft.addTable(peopleData, ['first_name', 'last_name', 'email_address', 'title'],
                ['First Name','Last Name', 'Email', 'Job Title'])
guiSalesLoft.addButton("Letter Frequency (Emails)", onclickFreqButton)
guiSalesLoft.addButton("Find Duplicates", onclickDuplicatesButton)
root.mainloop()