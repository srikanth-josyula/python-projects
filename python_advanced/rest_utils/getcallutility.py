# importing the requests library
import requests

# api-endpoint
url  = 'http://api.open-notify.org/astros.json'

# sending get request and saving the response as response object
r = requests.get(url)

# extracting data in json format
data = r.json()
  
for x in data['people']:
    name = x['name']
    craft = x['craft']
    
    # printing the output
    print("Name: %s\tCraft: %s"
      %(name, craft))

'''
r.content() # Return the raw bytes of the data payload
r.text() # Return a string representation of the data payload
r.json() # This method is convenient when the API returns JSON
'''