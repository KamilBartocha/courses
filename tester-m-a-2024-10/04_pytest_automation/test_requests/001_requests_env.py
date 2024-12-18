import requests
import pytest


@pytest.fixture
def api_url():
    return "https://simple-books-api.glitch.me"

def test_can_get_status(api_url):
    response = requests.get(api_url + "/status")
    assert response.status_code == 200
    body = response.json()
    assert body["status"] == "OK"
