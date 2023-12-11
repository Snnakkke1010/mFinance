import requests
import json

url = 'http://localhost:8000/api/auth/register/'
data = {
    "email": "mama@gmail.com",
    "first_name": "alex",
    "second_name": "hredil",
    "password": "snake1010",
    "password2": "snake1010"
}

headers = {
    'Content-Type': 'application/json'
}

response = requests.post(url, data=json.dumps(data), headers=headers)

print(response.status_code)
print(response.text)

