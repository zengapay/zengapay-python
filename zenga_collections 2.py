import requests
from pprint import pprint

url = " https://api.sandbox.zengapay.com/v1/transfers"

payload = {}
headers = {
  'Authorization': 'Bearer ZPYPUBK-20dc00d515b11b5b5247b923565859055bc60d1212ebcccab8344540867ce9f3'
}

response = requests.get(url=url, headers=headers, data=payload, verify=False)

data = response.json()

pprint(data, indent=1)