import json

people_json = '''
[
    {
        "name": "Aarav Mehta",
        "place": "Delhi",
        "email": "aarav.mehta@example.com"
    },
    {
        "name": "Sophia Roy",
        "place": "Mumbai",
        "email": "sophia.roy@example.com"
    }
]
'''

data = json.loads(people_json)

for person in data:
    print(person["name"])
for person in data:
    del (person["email"])
print(data)
