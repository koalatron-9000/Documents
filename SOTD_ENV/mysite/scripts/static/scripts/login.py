import requests
import json

url = "https://devapi.neonav.net/api/auth"

payload = json.dumps({
  "username": "piratesballkoala@gmail.com",
  "password": "c-3poislame!"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)