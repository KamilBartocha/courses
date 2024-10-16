import requests
import pytest

# base_url = 'https://simple-books-api.glitch.me'


# # response = requests.get('https://simple-books-api.glitch.me/status')
# response = requests.get(base_url + '/status')


# print(response)
# print(response.status_code)

# assert response.status_code == 200

# body = response.json()
# print(type(body))
# print(body)
# print(body['status'])

# # assert body['status'] == 'OK'

@pytest.fixture
def url_fixture():
    return 'https://simple-books-api.glitch.me'


def test_status(url_fixture):
    response = requests.get(url_fixture + '/status')
    assert response.status_code == 200

    body = response.json()
    assert body['status'] == 'OK'











# try:
#     response = requests.get(url)
#     if response.status_code == 200:
#         data = response.json()
#         print("Dane z serwera:", data)
#     else:
#         print("Błąd HTTP:", response.status_code)
# except requests.exceptions.RequestException as e:
#     print("Wystąpił błąd podczas wysyłania żądania:", e)
