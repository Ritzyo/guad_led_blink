import requests
import json

while True:
    res = requests.get('http://127.0.0.1:5000/')
    response = json.loads(res.text)
    print(response)

