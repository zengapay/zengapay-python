import requests
from pprint import pprint

url = " https://api.sandbox.zengapay.com/v1/collections"

payload = {
    "msisdn": "256788693374",
    "amount": 200000,
    "external_reference": "0000001889194",
    "narration": "Clearing Invoice - #0000001889194"
}
headers = {
  'Authorization': 'Bearer ZPYPUBK-20dc00d515b11b5b5247b923565859055bc60d1212ebcccab8344540867ce9f3'
}

response = requests.post(url=url, headers=headers, data=payload, verify=False)

data = response.json()

pprint(data, indent=1)