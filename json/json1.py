import json

with open("data.json", "r") as f:
    data = json.load(f)

for product in data["products"]:
    print(product["name"])
