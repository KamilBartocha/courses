import requests


ENDPOINT = "https://todo.pixegami.io"

def test_can_call_api():
    """Napisz podstawowy test, który sprawdzi czy api zwraca kod 200"""
    response = requests.get(url=ENDPOINT)
    print("ALAMAKOTA")
    print(response.status_code)
    assert response.status_code == 200

def test_can_create_task():
    """
    2. Napisz test, który stworzy task(create task)
    metoda: PUT endpoint: /create-task

    body:
    json
    {
    "content": "<string>",
    "user_id": "<string>",
    "is_done": False
    }
    """
    body = {"content": "umyj okna", "user_id": "ala ma kota", "is_done": False}
    response_put = requests.put(url=ENDPOINT + "/create-task", json=body)
    assert response_put.status_code == 200

def test_can_create_and_get_task():
    """1. create
       2. find id
       3. get"""
    body = {"content": "umyj okna", "user_id": "Zbyszek tester", "is_done": False}
    response_put = requests.put(url=ENDPOINT + "/create-task", json=body)
    assert response_put.status_code == 200
    my_id = response_put.json()["task"]["task_id"]
    print(my_id)

    response_get = requests.get(url=ENDPOINT + "/get-task/" + my_id)
    assert response_get.status_code


def test_can_list_tasks():
    body = {"content": "umyj okna", "user_id": "Zbyszek1", "is_done": False}
    response_put = requests.put(url=ENDPOINT + "/create-task", json=body)
    assert response_put.status_code == 200
    response_list = requests.get(url=ENDPOINT + "/list-tasks/" + "Zbyszek1")
    print(response_list.json())

"""
    {'task':
        {'user_id':
        'Zbyszek tester',
        'content': 'umyj okna',
        'is_done': False,
        'created_time': 1745673030,
        'task_id': 'task_c23d65e1024f4a319cdfaceda9b8b9e4',
        'ttl': 1745759430
        }
    }
"""