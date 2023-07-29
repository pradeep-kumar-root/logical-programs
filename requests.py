import requests
from requests.exceptions import HTTPError

try:
    res = requests.get('https://reqres.in/api/users?page=2',)
    print(res.status_code)
    print(res.headers)
    print(res.json())
    print(res.text)
    print(res.content)
    response.raise_for_status()
except HTTPError as e:
    print("HTTP error occured")
