import requests
import json
import sys

def get_user_info(u_id):
  if isinstance(u_id, int):
    user_id = str(u_id)
  else:
    user_id = str(u_id[1])
  url = "https://devapi.neonav.net/api/user/id"
  payload = json.dumps({
    "requestId": user_id
  })
  headers = {
    'x-access-token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjM3Njk3MTc2NzAiLCJ1c2VybmFtZSI6IlRoZSBCYWJhbG9uIFJvY2tlciIsInVwZGF0ZWQiOiIyMDIyLTA4LTI2VDIzOjQ1OjIwLjIzOFoiLCJpc3MiOiJuZW9uYXYubmV0IiwiaWF0IjoxNjc5MDE2ODY5LCJleHAiOjE2ODY3OTI4Njl9.Ax0rQlshBb1iOlOQOb0fIr64aeeWKg5iBNCmi_OR4Jg',
    'Content-Type': 'application/json'
  }

  response = requests.request("POST", url, headers=headers, data=payload)
  json_response = json.loads(response.text)
  response_id = json_response['id']
  response_user_name = json_response['name']
  response_first_name = json_response['meta']['firstname']
  response_last_name = json_response['meta']['lastname']

    #print(json_response)
  print('ID:' + response_id + '\n' 'First:' + response_first_name + ' ' + 'last:' + response_last_name + ' ' +'AKA:' + response_user_name)

if __name__ == "__main__":
    get_user_info(sys.argv)
