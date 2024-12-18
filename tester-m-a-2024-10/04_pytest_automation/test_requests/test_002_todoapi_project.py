import requests
import uuid

ENDPOINT = "https://todo.pixegami.io"

def test_can_call_api():
    response = requests.get(url=ENDPOINT)
    assert response.status_code == 200

    data = response.json()
    assert data['message'] == "Hello World from Todo API"

def test_can_create_task():
    body = {"content": "todo1",
            "user_id": "zbyszek1",
            "task_id": "Task01",
            "is_done": False
            }
    response = requests.put(url=ENDPOINT + "/create-task", json=body)
    assert response.status_code == 200

def test_can_create_and_get_task():
    body = {"content": "todo2",
            "user_id": "zbyszek2",
            "task_id": "Task01",
            "is_done": False
            }
    response_create = requests.put(url=ENDPOINT + "/create-task", json=body)
    assert response_create.status_code == 200

    create_data = response_create.json()
    task_id = create_data["task"]["task_id"]
    response_get = requests.get(url=ENDPOINT + "/get-task" + "/" + task_id)
    get_data = response_get.json()
    assert response_get.status_code == 200
    assert len(get_data) != 0
    assert get_data["task_id"] == task_id

def test_can_list_tasks():
    user_id = "test_list_user01"
    body = {"content": "todo2",
            "user_id": user_id,
            "task_id": "Task01",
            "is_done": False
            }
    response_create = requests.put(url=ENDPOINT + "/create-task", json=body)
    assert response_create.status_code == 200

    response = requests.get(url=ENDPOINT + "/list-tasks" + "/" + user_id)
    assert response.status_code == 200
    assert len(response.json()["tasks"]) != 0

def test_can_update_task():
    body = {"content": "todo2",
            "user_id": "zbyszek4",
            "task_id": "Task01",
            "is_done": False
            }
    response_create = requests.put(url=ENDPOINT + "/create-task", json=body)
    assert response_create.status_code == 200

    create_data = response_create.json()
    task_id = create_data["task"]["task_id"]
    new_var_is_done = True
    body_update = {"content": "todo2",
                  "user_id": "zbyszek4",
                  "task_id": task_id,
                  "is_done": new_var_is_done
                  }
    response_update = requests.put(url=ENDPOINT + "/update-task", json=body_update)
    assert response_update.status_code == 200

    response_get = requests.get(url=ENDPOINT + "/get-task" + "/" + task_id)
    assert response_get.status_code == 200
    get_data = response_get.json()
    assert get_data["is_done"] == new_var_is_done

def test_can_delete_task():
    user_id = str(uuid.uuid4())
    body = {"content": "todo2",
            "user_id": user_id,
            "task_id": "Task01",
            "is_done": False
            }
    response_create = requests.put(url=ENDPOINT + "/create-task", json=body)
    assert response_create.status_code == 200

    create_data = response_create.json()
    task_id = create_data["task"]["task_id"]
    response_get = requests.get(url=ENDPOINT + "/get-task" + "/" + task_id)
    get_data = response_get.json()
    assert response_get.status_code == 200
    assert len(get_data) != 0
    assert get_data["task_id"] == task_id

    response_delete = requests.delete(url=ENDPOINT + "/delete-task" + "/" + task_id)
    assert response_delete.status_code == 200

    response_get = requests.get(url=ENDPOINT + "/get-task" + "/" + task_id)
    get_data = response_get.json()
    assert response_get.status_code == 404
    assert get_data["detail"] == f'Task {task_id} not found'

    response_list = requests.get(url=ENDPOINT + "/list-tasks" + "/" + user_id)
    assert len(response_list.json()["tasks"]) == 0
