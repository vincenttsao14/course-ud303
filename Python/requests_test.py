import requests
uri = "http://swapi.co/api/people/1/"
uri2 = "http://uinames.com/api?ext&region=Spain"
a = requests.get(uri2)
print(a.json())
print(type(a))
print(a.status_code)
