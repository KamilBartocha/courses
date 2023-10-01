from helpers_requests import *

ENDPOINT = "https://todo.pixegami.io/"

def test_can_call_api():
    response = send_request(ENDPOINT)
    assert response.status_code == 200

def test_can_create_task():
    payload = {"content": "ala_cb",
               "user_id": "tester_cb",
               "is_done": False
              }
    response = create_task(ENDPOINT, payload)
    assert response.status_code == 200

def test_can_update_task():
    payload = {"content": "update_cb",
               "user_id": "update_cb",
               "is_done": False
              }
    response = create_task(ENDPOINT, payload)
    assert response.status_code == 200
    data = response.json()
    task_id = data["task"]["task_id"]
    new_payload = {"user_id": "update_cb",
                   "task_id": task_id,
                   "is_done": True,
                   "content": "new_content"
                  }
    update_response = update_task(ENDPOINT, new_payload)
    assert update_response.status_code == 200

    get_task_response = get_task(ENDPOINT, task_id)
    assert get_task_response.status_code == 200

    data_after_update = get_task_response.json()
    assert data_after_update["content"] == new_payload["content"]
    assert data_after_update["is_done"] == new_payload["is_done"]

def test_can_delete_task():
    payload = {"content": "update_cb",
               "user_id": "update_cb",
               "is_done": False
              }
    response = create_task(ENDPOINT, payload)
    assert response.status_code == 200
    data = response.json()
    task_id = data["task"]["task_id"]

    delete_response = delete_task(ENDPOINT, task_id)
    assert delete_response.status_code == 200

    get_task_response = get_task(ENDPOINT, task_id)
    assert get_task_response.status_code == 404
