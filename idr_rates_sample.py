import requests

source = requests.get(url='http://www.floatrates.com/daily/usd.json')
json_data = source.json().values()

for data in json_data:
    code = data['code']
    name = data['name']
    date = data['date']
    inverse_rate = data['inverseRate']

    print('Code:', code)
    print("Name :", name)
    print("Date :", date)
    print("Inverse Rate:", inverse_rate)