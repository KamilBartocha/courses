import requests

base_url = "https://todo.pixegami.io/"

response = requests.get(url=base_url)
print(response.status_code)
print(response.text)

data = response.json()
print(data["message"])
print(type(data))
