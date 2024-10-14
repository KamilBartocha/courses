from helpers_requests import *

ENDPOINT = "https://todo.pixegami.io/"

def test_can_call_api():
    response = send_request(ENDPOINT)
    assert response.status_code == 200
