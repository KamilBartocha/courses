import requests
import random

ENDPOINT = "https://todo.pixegami.io"

def test_can_call_api():
    response = requests.get(url=ENDPOINT)
    code_response = response.status_code
    assert code_response == 200

def test_api_returns_404_for_bad_url():
    response = requests.get(url=ENDPOINT + "/status")
    assert response.status_code == 404

def test_api_returns_hello_msg():
    expected = "Hello World from Todo API"
    response = requests.get(url=ENDPOINT)
    body = response.json()
    assert expected == body["message"]

def test_api_returns_not_found_for_bad_url():
    response = requests.get(url=ENDPOINT + "/status")
    body = response.json()
    expected = "Not Found"
    assert expected == body["detail"]

def test_api_returns_not_found_for_bad_url2():
    bad_url = ENDPOINT + "/nieistnieje"
    response = requests.get(bad_url)
    body = response.json()
    expected = {"detail":"Not Found"}
    assert expected == body

def test_can_create_task():
    req_body = {"content": "Nakarm kota",
                "user_id": "Alamakota",
                "task_id": "01",
                "is_done": False
               }
    response_put = requests.put(url=ENDPOINT + "/create-task", json=req_body)
    assert response_put.status_code == 200

    response_body = response_put.json()
    assert response_body["task"]["user_id"] == "Alamakota"
    assert response_body["task"]["content"] == "Nakarm kota"
    assert response_body["task"]["is_done"] == False


def test_not_existing_task_id_returns_404():
    response = requests.get(url=ENDPOINT + "/get-task/" + "task_not_existing")
    assert response.status_code == 404


def test_can_create_and_get_task():
    task_body = {"content": "Nakarm kota",
                 "user_id": "Alamakota_tmp",
                 "task_id": "01",
                 "is_done": False
                }
    response_create = requests.put(url=ENDPOINT + "/create-task", json=task_body)
    assert response_create.status_code == 200
    body_create_response = response_create.json()
    unique_task_id = body_create_response["task"]["task_id"]
    response = requests.get(url=ENDPOINT + "/get-task/" + unique_task_id)
    assert response.status_code == 200
    assert response.json()['task_id'] == unique_task_id

def test_can_list_tasks():
    radom_user = "Alamakota_tmp_" + str(random.randint(1000000, 9999999))
    task_body = {"content": "Nakarm kota",
                 "user_id": radom_user,
                 "task_id": "01",
                 "is_done": False
                }
    response_create = requests.put(url=ENDPOINT + "/create-task", json=task_body)
    assert response_create.status_code == 200

    response = requests.get(url=ENDPOINT + "/list-tasks/" + radom_user)
    assert response.status_code == 200

    body = response.json()
    tasks = body["tasks"]
    assert isinstance(tasks, list)
    assert len(tasks) > 0

def test_can_update_task():
    task_body = {"content": "Nakarm kota",
                 "user_id": "Alamakota_1",
                 "task_id": "01",
                 "is_done": False
                }
    response_create = requests.put(url=ENDPOINT + "/create-task", json=task_body)
    assert response_create.status_code == 200
    body_create_response = response_create.json()
    unique_task_id = body_create_response["task"]["task_id"]

    updated_body = {"content": "Nakarm kota",
                    "user_id": "Alamakota_1",
                    "task_id": unique_task_id,
                    "is_done": True
                    }
    response_update = requests.put(url=ENDPOINT + "/update-task", json=updated_body)
    assert response_update.status_code == 200

    response = requests.get(url=ENDPOINT + "/get-task/" + unique_task_id)
    assert response.status_code == 200
    body = response.json()
    assert body["is_done"] == True

def test_can_delete_task():
    task_body = {"content": "Nakarm kota",
                 "user_id": "Alamakota_2",
                 "task_id": "01",
                 "is_done": False
                }
    response_create = requests.put(url=ENDPOINT + "/create-task", json=task_body)
    assert response_create.status_code == 200
    body_create_response = response_create.json()
    unique_task_id = body_create_response["task"]["task_id"]
    print(unique_task_id)

    response_delete = requests.delete(url=ENDPOINT + "/delete-task/" + unique_task_id)
    assert response_delete.status_code == 200

    response = requests.get(url=ENDPOINT + "/get-task/" + unique_task_id)
    assert response.status_code == 404
    msg =  response.json()["detail"]
    assert msg == f"Task {unique_task_id} not found"

def test_list_empty():
    """
    1.list tasks for random user
    2.response body should be empty
    """
    pass

def test_list_empty():
    """
    1.Create 10 tasks for user
    2.response body list should contain 10 tasks
    """
    pass
