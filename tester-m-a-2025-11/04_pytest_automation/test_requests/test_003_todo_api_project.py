import requests
import random

ENDPOINT = r"https://todo.pixegami.io/"


def test_can_call_api():
    """1. Napisz podstawowy test, który sprawdzi czy api zwraca kod 200"""
    res = requests.get(url=ENDPOINT)
    status = res.status_code
    print(status)
    assert status == 200


def test_bad_url_returns_404():
    """1. Napisz podstawowy test, który sprawdzi czy api zwraca kod 404 dla
    https://todo.pixegami.io/status"""
    response = requests.get(url=ENDPOINT + "status")
    assert response.status_code == 404


def test_api_root_shows_hello_msg():
    """1. Napisz test, który sprawdzi czy api zwraca body z
    wiadomością: {"message":"Hello World from Todo API"}"""
    response = requests.get(url=ENDPOINT)
    body = response.json()
    assert body["message"] == "Hello World from Todo API"


def test_api_root_shows_not_found_for_bad_url():
    """1. Napisz test, który sprawdzi czy api zwraca body z
    wiadomością: {"detail":"Not Found"} dla złego url"""
    response = requests.get(url=ENDPOINT + "status")
    body = response.json()
    assert body["detail"] == "Not Found"


def test_can_create_task():
    """2. Napisz test, który stworzy task(create task)"""
    data = {"content": "Kot", "user_id": "Ala", "task_id": "Ala1", "is_done": False}
    response = requests.put(url=ENDPOINT + "create-task", json=data)
    assert response.status_code == 200
    """
    responose body
    {
        "task": {
            "user_id": "Ala",
            "content": "Kot",
            "is_done": false,
            "created_time": 1768049729,
            "task_id": "task_4ef4eb63a74c46e1a0fbc54ecbe7068b",
            "ttl": 1768136129
        }
    }
    """
    body = response.json()
    assert body["task"]["user_id"] == data["user_id"]
    assert body["task"]["content"] == data["content"]
    assert body["task"]["is_done"] == data["is_done"]


def test_can_get_task():
    data = {
        "content": "Kot",
        "user_id": "Ala_tmp",
        "task_id": "Ala1_tmp",
        "is_done": False,
    }
    create_task = requests.put(url=ENDPOINT + "create-task", json=data)
    assert create_task.status_code == 200

    body = create_task.json()
    task_id = body["task"]["task_id"]
    print(task_id)

    response = requests.get(url=ENDPOINT + "get-task/" + task_id)
    assert response.status_code == 200
    assert response.json()["task_id"] == task_id
    """
    Response body
    {
        "is_done": false,
        "content": "string",
        "ttl": 1768134136,
        "user_id": "string",
        "task_id": "task_4ef4eb63a74c46e1a0fbc54ecbe7068b",
        "created_time": 1768047736
    }
    """


def test_not_existing_task_id_returns_404():
    task_id = "not_existing_task_id"
    response = requests.get(url=ENDPOINT + "get-task/" + task_id)
    assert response.status_code == 404
    body_not_found_task = response.json()
    print(body_not_found_task)
    assert body_not_found_task["detail"] == f"Task {task_id} not found"


def test_can_list_tasks():
    """Get all tasks for a user 'Ala'
    GET /list-tasks/{user_id}"""
    user_name = f"Ala_{random.randint(1_000_000, 9_999_999)}"
    data = {
        "content": "Kot",
        "user_id": user_name,
        "task_id": "Ala1_tmp",
        "is_done": False,
    }
    create_task = requests.put(url=ENDPOINT + "create-task", json=data)
    assert create_task.status_code == 200

    response = requests.get(url=ENDPOINT + "list-tasks" + "/" + user_name)
    assert response.status_code == 200

    body = response.json()["tasks"]
    assert len(body) == 1
    assert body[0]["user_id"] == user_name


def test_can_update_task():
    # 1 create task
    user_name = f"Ala2_{random.randint(1_000_000, 9_999_999)}"
    data = {
        "content": "Kot",
        "user_id": user_name,
        "task_id": "Ala1_tmp",
        "is_done": False,
    }
    create_task = requests.put(url=ENDPOINT + "create-task", json=data)
    assert create_task.status_code == 200
    task_name = create_task.json()["task"]["task_id"]

    # 2 update task
    data_updated = {
        "content": "Pies",
        "user_id": user_name,
        "task_id": task_name,
        "is_done": True,
    }
    response_update = requests.put(url=ENDPOINT + "update-task", json=data_updated)
    assert response_update.status_code == 200

    # 3 sprawdz czy nowe wartości(get)
    response_get = requests.get(url=ENDPOINT + "get-task/" + task_name)
    assert response_get.status_code == 200
    body_res_get = response_get.json()
    assert body_res_get["content"] == "Pies"
    assert body_res_get["is_done"]


def test_can_delete_task():
    # 1 create task
    user_name = f"Ala3_{random.randint(1_000_000, 9_999_999)}"
    data = {
        "content": "Kot",
        "user_id": user_name,
        "task_id": "Ala1_tmp",
        "is_done": False,
    }
    create_task = requests.put(url=ENDPOINT + "create-task", json=data)
    assert create_task.status_code == 200
    task_name = create_task.json()["task"]["task_id"]

    # 2. delete task: DELETE /delete-task/{task_id}
    response_delete = requests.delete(url=ENDPOINT + "delete-task" + "/" + task_name)
    assert response_delete.status_code == 200

    # 3. sprawdz czy nie ma
    response = requests.get(url=ENDPOINT + "get-task/" + task_name)
    assert response.status_code == 404
    body_not_found_task = response.json()
    assert body_not_found_task["detail"] == f"Task {task_name} not found"
