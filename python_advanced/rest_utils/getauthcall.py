# importing the requests library
import requests

# Case - 1 Basic Auth
url = 'http://api.open-notify.org/astros.json'
authheaders = HTTPBasicAuth('username', 'password')
response = requests.get(url, auth=authheaders)

if (response.status_code == 200):
    print("The request was a success!")
    # Code here will only run if the request is successful
elif (response.status_code == 404):
    print("Result not found!")
    # Code here will react to failed requests

# Case - 2 Bearer Token
url = 'http://api.open-notify.org/astros.json'
my_headers = {'Authorization' : 'Bearer {access_token}'}
response = requests.get('http://httpbin.org/headers', headers=my_headers)
if (response.status_code == 200):
    print("The request was a success!")
    # Code here will only run if the request is successful
elif (response.status_code == 404):
    print("Result not found!")
    # Code here will react to failed requests