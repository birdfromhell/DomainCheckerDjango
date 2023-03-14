import json
import requests

domain = 'ababil-mustax.me'
url = "https://domain-checker7.p.rapidapi.com/whois"

querystring = {"domain": domain}

headers = {
    "X-RapidAPI-Key": "fe7ac125c5msh94f9c196609b1eep12fb18jsndc6f9e5920c3",
    "X-RapidAPI-Host": "domain-checker7.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

x = json.dumps(response.json())
z = json.loads(x)
print(z)
