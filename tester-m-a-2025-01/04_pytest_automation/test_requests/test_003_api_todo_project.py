import requests

ENDPOINT = 'https://todo.pixegami.io'

def test_can_call_api():
    response = requests.get(url=ENDPOINT)
    assert response.status_code == 200

def test_can_create_task():
    # request
    # metoda put,
    # endpoint https://todo.pixegami.io/create-task
    # body - json z
    #     {
    #    "content": "string",
    #    "user_id": "string",
    #    "task_id": "string",
    #    "is_done": false
    #    }

    # 1) create task
    # 2) check if status code == 200
    body_req = {
       "content": "string1",
       "user_id": "Franek Tester",
       "task_id": "string2",
       "is_done": False
    }
    response = requests.put(url=ENDPOINT + "/create-task", json=body_req)
    assert response.status_code == 200

    response_body = response.json()
    print(response_body)
    """{'task':
            {
            'user_id': 'Franek Tester',
            'content': 'string1',
            'is_done': False,
            'created_time': 1742324475,
            'task_id': 'task_303c4c3bb0174bdfa9334a6f3ecf04a4',
            'ttl': 1742410875
            }
        }
    """
def test_can_create_and_get_task_1():
    """
    3. check get-task endpoint for 2. task_id
    4. check statuscode
    """
    response = requests.get(url=ENDPOINT + "/get-task" + "/" + "task_303c4c3bb0174bdfa9334a6f3ecf04a4")
    print(response.json())
    """{
       'is_done': False,
        'content': 'string1',
        'ttl': 1742410875,
        'user_id': 'Franek Tester',
        'task_id': 'task_303c4c3bb0174bdfa9334a6f3ecf04a4',
        'created_time': 1742324475
       }"""



def test_can_create_and_get_task_2():
    """ 1. Create task
        2. get task_id
        3. check get-task endpoint for 2. task_id
        4. check statuscode
    """
    #1
    body_req = {
       "content": "string1",
       "user_id": "Franek Tester2",
       "task_id": "string2",
       "is_done": False
    }
    response = requests.put(url=ENDPOINT + "/create-task", json=body_req)
    assert response.status_code == 200
    response_body = response.json()
    #2
    id = response_body["task"]["task_id"]
    #3
    response_get = requests.get(url=ENDPOINT + "/get-task" + "/" + id)
    #4
    assert response_get.status_code == 200
    id_returned = response_get.json()["task_id"]
    assert id == id_returned


def test_can_list_task():
    tester = "Franek1"
    body_req = {
       "content": "string1",
       "user_id": tester,
       "task_id": "string2",
       "is_done": False
    }
    response = requests.put(url=ENDPOINT + "/create-task", json=body_req)
    assert response.status_code == 200

    response_list = requests.get(url=ENDPOINT + '/list-tasks/' + tester)
    assert response_list.status_code == 200

    tasks_len = len(response_list.json()["tasks"])
    assert tasks_len > 0
