import pytest
import requests

BASE_URL = "https://simple-books-api.click"
API_TOKEN = ""

HEADERS = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json"
}

@pytest.fixture
def get_api_token():
    url = f"{BASE_URL}/api-clients/"
    payload = {
        "clientName": "Alamakota201",
        "clientEmail": "alamakota201@example.com"
    }
    response = requests.post(url, json=payload)
    assert response.status_code == 201
    token = response.json()['accessToken']
    global API_TOKEN
    API_TOKEN = token
    return token

def test_status():
    response = requests.get(f"{BASE_URL}/status")
    assert response.status_code == 200
    assert response.json()["status"] == "OK"

def test_create_order(get_api_token):
    url = f"{BASE_URL}/orders"
    payload = {
        "bookId": 1,
        "customerName": "John"
    }
    headers = {
        "Authorization": f"Bearer {get_api_token}",
        "Content-Type": "application/json"
    }
    response = requests.post(url, json=payload, headers=headers)
    assert response.status_code == 201
    assert "orderId" in response.json()
