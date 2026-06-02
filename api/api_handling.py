import requests

response = requests.get(
    "https://api.freeapi.app/api/v1/public/randomproducts/product/random"
)

data = response.json()

from pprint import pprint
pprint(data)

product = data["data"]["category"]
print(product)
