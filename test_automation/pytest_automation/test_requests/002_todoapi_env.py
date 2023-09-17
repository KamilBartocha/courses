import requests

ENDPOINT = "https://todo.pixegami.io/"


def test_can_call_api():
    response = requests.get(ENDPOINT)
    assert response.status_code == 200

def test_can_create_task():
    payload = {
        "content": "test",
        "user_id": "tester",
        "is_done": False
    }
    response = requests.put(ENDPOINT + "/create-task", json=payload)
    assert response.status_code == 200
    data = response.json()

    task_id = data["task"]["task_id"]
    get_response = requests.get(ENDPOINT + "/get-task/" + task_id)

    assert get_response.status_code == 200
    get_task_data = get_response.json()
    assert get_task_data["content"] == payload["content"]
    assert get_task_data["user_id"] == payload["user_id"]


def test_can_update_task():
    payload = {
        "content": "test",
        "user_id": "tester",
        "is_done": False
    }
    response = requests.put(ENDPOINT + "/create-task", json=payload)
    task_id = response.json()["task"]["task_id"]
    new_payload = {
        "user_id": "tester",
        "task_id": task_id,
        "is_done": True,
        "content": "updated_content"
    }
    update_response = requests.put(ENDPOINT + "/update-task", json=new_payload)
    assert update_response.status_code == 200
    get_response = requests.get(ENDPOINT + "/get-task/" + task_id)
    get_task_data = get_response.json()
    assert get_task_data["content"] == new_payload["content"]
    assert get_task_data["is_done"] == new_payload["is_done"]

def test_can_delete_task():
    payload = {
        "content": "test",
        "user_id": "tester",
        "is_done": False
    }
    response = requests.put(ENDPOINT + "/create-task", json=payload)
    task_id = response.json()["task"]["task_id"]
    delete_response = requests.delete(ENDPOINT + "/delete-task/" + task_id)
    assert delete_response.status_code == 200

    get_task_response = requests.get(ENDPOINT + "/get-task/" + task_id)
    assert get_task_response.status_code == 404
