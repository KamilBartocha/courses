import pytest
import requests

BASE_URL = "https://simple-books-api.glitch.me"
API_TOKEN = ""

HEADERS = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json"
}

@pytest.fixture
def get_api_token():
    url = f"{BASE_URL}/api-clients/"
    payload = {
        "clientName": "Alamakota2025",
        "clientEmail": "alamakota2025@example.com"
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

def test_list_books():
    response = requests.get(f"{BASE_URL}/books")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_list_books_with_query_params():
    params = {"type": "fiction", "limit": 5}
    response = requests.get(f"{BASE_URL}/books", params=params)
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) <= 5

def test_get_single_book():
    book_id = 1
    response = requests.get(f"{BASE_URL}/books/{book_id}")
    assert response.status_code == 200
    assert response.json()["id"] == book_id

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

