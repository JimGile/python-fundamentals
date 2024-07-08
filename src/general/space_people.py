import requests

people = requests.get('http://api.open-notify.org/astros.json')
json = people.json()

print(json)

print('People in space:')
for p in json['people']:
    print(p['name'])
