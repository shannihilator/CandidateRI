import os
authKey = os.environ['KEY']

import requests


urlPeople = "https://api.salesloft.com/v2/people.json"

headers = { 
    'Authorization' : 'Bearer ' + authKey 
}
  
r = requests.get(urlPeople, headers = headers  ) 
print(r)

data = r.json()
print(data)