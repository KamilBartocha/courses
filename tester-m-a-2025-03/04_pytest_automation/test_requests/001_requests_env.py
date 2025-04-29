import requests

baseUrl = "https://simple-books-api.glitch.me"

def test_get_status():
    response_get = requests.get(baseUrl + "/status")
    print(response_get.json())
    print(response_get.status_code)
    assert response_get.status_code == 200


def test_get_status_negative():
    response_get = requests.get(baseUrl + "/statu")
    print(response_get.status_code)
    assert response_get.status_code == 404
