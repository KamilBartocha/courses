import requests

def send_request(ENDPOINT):
    return requests.get(url=ENDPOINT)
