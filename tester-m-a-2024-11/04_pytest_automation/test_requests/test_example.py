import requests
import pytest
BASE_URL = "https://simple-books-api.glitch.me"
API_TOKEN = 'f0125bfb7eed22d2d9a60a0fe1defbe45064d589d5a19b9c51a5715c874c4ed0'

@pytest.fixture
def can_use_token():
    pass


def test_create_order(can_use_token):
    """ Test to submit a new order. """
    url = f"{BASE_URL}/orders"
    payload = {
        "bookId": 1,
        "customerName": "John"
    }
    headers = {
        "Authorization": f"Bearer {API_TOKEN}",
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)
    assert response.status_code == 201