import requests


ENDPOINT = "https://todo.pixegami.io"

def test_can_call_api():
    response = requests.get(ENDPOINT)
    code = response.status_code
    assert code == 200

def test_can_create_task():
    test_user_id = "Ala Kowalska"
    data = {
        "content": "my_task_ala_ma_kota",
        "user_id": test_user_id,
        "task_id": "Ala_task1",
        "is_done": False
    }
    response = requests.put(url=ENDPOINT + "/create-task", json=data)
    response_body = response.json()
    assert response.status_code == 200
    created_user = response_body["task"]["user_id"]
    print(response_body)
    assert test_user_id == created_user

def test_can_get_task():
    """
    create-task body:
    {'task':
            {
            'user_id': 'Ala Kowalska',
            'content': 'my_task_for_get_test',
            'is_done': False,
            'created_time': 1737806493,
            'task_id': 'task_042ba861d28446e9892524bff31c9139',
            'ttl': 1737892893
            }
        }

    get-task - body:
    {'is_done': False,
    'content': 'my_task_for_get_test',
    'ttl': 1737893450,
    'user_id':'Ala Kowalska',
    'task_id': 'task_13ea927b0775451eb9227293c35e9b04',
    'created_time': 1737807050}

    """
    test_user_id = "Ala Kowalska"
    test_content = "my_task_for_get_test"
    data = {
        "content": test_content,
        "user_id": test_user_id,
        "task_id": "Ala_task2",
        "is_done": False
    }
    response_create = requests.put(url=ENDPOINT + "/create-task", json=data)
    assert response_create.status_code == 200
    response_create_body = response_create.json()
    # print(response_create_body)
    unique_task_id = response_create_body["task"]["task_id"]
    print(unique_task_id)


    response_get = requests.get(ENDPOINT + "/get-task" + "/" + unique_task_id)
    assert response_get.status_code == 200
    get_res_body = response_get.json()
    print(get_res_body)
    assert get_res_body["content"] == test_content
    assert get_res_body["user_id"] == test_user_id
    assert get_res_body["is_done"] == False

import uuid

def test_can_list_tasks():
    # DOKUMENTACJA: GET /list-tasks/user_id
    # 1)create task
    # 2)get list of tasks for user from 1)
    # assert status code == 200
    # assert 2) body is not empty
    # print(uuid.uuid4())
    pass