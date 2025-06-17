import requests

baseUrl = "https://simple-books-api.glitch.me"

def test_status_200():
    assert requests.get(baseUrl + "/status").status_code == 200

def test_get_status_negative():
    response_get = requests.get(baseUrl + "/statu")
    print(response_get.status_code)
    assert response_get.status_code == 404
