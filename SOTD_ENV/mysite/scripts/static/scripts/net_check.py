import requests
def netcheck():
    url = "https://devapi.neonav.net/api/auth/netcheck"
    payload={}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)

if __name__ == "__main__":
    netcheck()