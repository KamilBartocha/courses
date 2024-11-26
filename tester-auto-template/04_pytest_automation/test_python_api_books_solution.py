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
    """ Fixture to register an API client and retrieve an access token. """
    url = f"{BASE_URL}/api-clients/"
    payload = {
        "clientName": "Postman",
        "clientEmail": "example@example.com"
    }
    response = requests.post(url, json=payload)
    assert response.status_code == 201
    token = response.json()['accessToken']
    global API_TOKEN
    API_TOKEN = token
    return token

def test_status():
    """ Test the status endpoint to ensure API is running. """
    response = requests.get(f"{BASE_URL}/status")
    assert response.status_code == 200
    assert response.json()["status"] == "OK"

def test_list_books():
    """ Test to retrieve the list of books. """
    response = requests.get(f"{BASE_URL}/books")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_list_books_with_query_params():
    """ Test to retrieve list of fiction books with a limit of 5. """
    params = {"type": "fiction", "limit": 5}
    response = requests.get(f"{BASE_URL}/books", params=params)
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) <= 5

def test_get_single_book():
    """ Test to retrieve a single book by ID. """
    book_id = 1
    response = requests.get(f"{BASE_URL}/books/{book_id}")
    assert response.status_code == 200
    assert response.json()["id"] == book_id

def test_create_order(get_api_token):
    """ Test to submit a new order. """
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

def test_get_all_orders(get_api_token):
    """ Test to retrieve all orders. """
    url = f"{BASE_URL}/orders"
    headers = {
        "Authorization": f"Bearer {get_api_token}"
    }
    response = requests.get(url, headers=headers)
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_single_order(get_api_token):
    """ Test to retrieve a single order by order ID. """
    url = f"{BASE_URL}/orders"
    payload = {
        "bookId": 1,
        "customerName": "John"
    }
    headers = {
        "Authorization": f"Bearer {get_api_token}",
        "Content-Type": "application/json"
    }
    create_response = requests.post(url, json=payload, headers=headers)
    order_id = create_response.json()["orderId"]

    response = requests.get(f"{BASE_URL}/orders/{order_id}", headers=headers)
    assert response.status_code == 200
    assert response.json()["id"] == order_id

def test_update_order(get_api_token):
    """ Test to update an existing order. """
    url = f"{BASE_URL}/orders"
    payload = {
        "bookId": 1,
        "customerName": "John"
    }
    headers = {
        "Authorization": f"Bearer {get_api_token}",
        "Content-Type": "application/json"
    }
    create_response = requests.post(url, json=payload, headers=headers)
    order_id = create_response.json()["orderId"]

    patch_url = f"{BASE_URL}/orders/{order_id}"
    patch_payload = {"customerName": "Jane"}
    patch_response = requests.patch(patch_url, json=patch_payload, headers=headers)

    assert patch_response.status_code == 204

def test_delete_order(get_api_token):
    """ Test to delete an existing order. """
    url = f"{BASE_URL}/orders"
    payload = {
        "bookId": 1,
        "customerName": "John"
    }
    headers = {
        "Authorization": f"Bearer {get_api_token}",
        "Content-Type": "application/json"
    }
    create_response = requests.post(url, json=payload, headers=headers)
    order_id = create_response.json()["orderId"]

    delete_url = f"{BASE_URL}/orders/{order_id}"
    delete_response = requests.delete(delete_url, headers=headers)

    assert delete_response.status_code == 204
