import requests
ENDPOINT = "https://todo.pixegami.io"

def test_can_call_api():
    response = requests.get(url=ENDPOINT)
    assert response.status_code == 200

def test_can_create_task_data():
    body = {"content": "string",
            "user_id": "string",
            "task_id": "string",
            "is_done": False
            }
    response = requests.put(url=ENDPOINT + '/create-task', json=body)
    assert response.status_code == 200

def test_can_create_and_get_task():
    body =  {"content": "email",
            "user_id": "alamakota",
            "task_id": "name",
            "is_done": False
            }
    response_create = requests.put(url=ENDPOINT + '/create-task', json=body)
    assert response_create.status_code == 200
    unique_task_id = response_create.json()['task']['task_id']
    response_get = requests.get(url=ENDPOINT + '/get-task/' + unique_task_id)
    assert response_get.status_code == 200
    assert len(response_get.json()) != 0

def test_can_list_tasks():
    test_user = "Tester1"
    body =  {"content": "email",
            "user_id": test_user,
            "task_id": "name",
            "is_done": False
            }
    response_create = requests.put(url=ENDPOINT + '/create-task', json=body)
    assert response_create.status_code == 200
    response = requests.get(url=ENDPOINT + '/list-tasks/' + test_user)
    print(len(response.json()['tasks']))
    assert response.status_code == 200
    assert response.json() is not None

def test_can_update_task():
    new_content = 'send_email'
    body =  {"content": "email",
            "user_id": "alamakota",
            "task_id": "name",
            "is_done": False
            }
    new_body =  {"content": new_content,
                "user_id": "alamakota",
                "task_id": "name",
                "is_done": False
                }
    response_create = requests.put(url=ENDPOINT + '/create-task', json=body)
    assert response_create.status_code == 200
    unique_task_id = response_create.json()['task']['task_id']
    new_body["task_id"] = unique_task_id
    new_body["is_done"] = True

    response_update = requests.put(url=ENDPOINT + '/update-task', json=new_body)
    assert response_update.status_code == 200

    response_get_after = requests.get(url=ENDPOINT + '/get-task/' + unique_task_id)
    assert response_get_after.status_code == 200
    assert response_get_after.json()['content'] == new_content

def test_can_delete_task():
    task_id = 'task_id_300'
    body =  {"content": "email",
            "user_id": "alamakota20000",
            "task_id": task_id,
            "is_done": False
            }
    response_create = requests.put(url=ENDPOINT + '/create-task', json=body)
    assert response_create.status_code == 200
    unique_task_id = response_create.json()['task']['task_id']
    response_delete = requests.delete(url=ENDPOINT + '/delete-task/' + unique_task_id)
    assert response_delete.status_code == 200
    response_get = requests.get(url=ENDPOINT + '/get-task/' + unique_task_id)
    assert response_get.status_code == 404
