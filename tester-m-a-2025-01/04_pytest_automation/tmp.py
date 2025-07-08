import time
import pytest
import requests

api_url = "https://simple-books-api.glitch.me/status"
response_get = requests.get(url=api_url)

response_status = response_get.status_code  ## 200
print(response_status)
print(type(response_status))
assert response_status == 200


print(response_get.json())
print(type(response_get.json()))
print(response_get.json()["status"]) # OK

response_body = response_get.json() #{'status': 'OK'}
print(response_body)

assert response_body["status"] == "OK"
