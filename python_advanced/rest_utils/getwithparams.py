# importing the requests library
import requests

# api-endpoint
query = {'lat':'45', 'lon':'180'}
url = 'http://api.open-notify.org/iss-pass.json'
response = requests.get(url, params=query)

# extracting data in json format
data = response.json()
  
for x in data['response']:
    name = x['duration']
    craft = x['risetime']
    
    # printing the output
    print("Duration: %s\tRisetime: %s"
      %(name, craft))