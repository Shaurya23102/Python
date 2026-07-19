import requests
import json

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)
try:
    if response.status_code == 200:
        data = response.json()
    else:
        print("Error:", response.status_code)
except Exception as e:
    print("Exception occurred:", e)

abc = []
for user in data:
    entry = {
        "name": user.get("name"),
        "email_id": user.get("email"),
        "city": user.get("address", {}).get("city")
    }
    abc.append(entry)

with open("abc.json", "w") as f:
    json.dump(abc, f, indent=4)

with open("abc.json", "r") as f:
    new = json.load(f)

print(new)
