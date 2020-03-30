import requests

response = requests.get(url='https://reqres.in/api/users')
parsedResponse = response.json()
for user in parsedResponse['data']:
    print(user['email'])
