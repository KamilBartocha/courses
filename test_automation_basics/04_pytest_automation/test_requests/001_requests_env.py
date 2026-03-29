import requests

url = r"https://simple-books-api.click/"

response = requests.get(url)
print(response)  # object
print(response.status_code)

print(response.json())
print(type(response.json()))
