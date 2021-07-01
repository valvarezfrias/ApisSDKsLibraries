import requests

url = 'https://accounts.spotify.com/api/token' #url for authorization
data = {'title': 'Special Agent', 'body': 'Leroy Jethro Gibbs', 'userId': 1}

id = '97f80bee2862417da0a81014d26407bd'
secret = '36fb2f9eb3c344848df4b4dac98e89a7'

response = requests.post(url,{'grant_type':'client_credentials', 
                              #^^must be set this way according to spotify api
                              'client_id':id, #request login id
                              'client_secret':secret,}) #request login pass

print(response.status_code)
print(response.json()) #the user grants access so it prints access_token,token_type,
                       #expires_in (AS A DICT)