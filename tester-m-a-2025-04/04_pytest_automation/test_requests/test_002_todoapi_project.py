import requests

ENDPOINT = "https://todo.pixegami.io"


def test_can_call_api():
    response = requests.get(url=ENDPOINT)
    assert response.status_code == 200

def test_api_returns_hello_msg():
    expected_msg = "Hello World from Todo API"
    response = requests.get(url=ENDPOINT)
    actual_msg = response.json()["message"]     # dict: {'message': 'Hello World from Todo API'}
    assert expected_msg == actual_msg

def test_can_create_task():
    """
    {
        "content": "string",
        "user_id": "string",
        "task_id": "string",
        "is_done": false
    }

    response_body:

    {'task':
        {'user_id': 'Alamakota',
         'content': 'make app',
         'is_done': False,
         'created_time': 1750090208,
         'task_id': 'task_f37bbfbe46e2443c8571102ddd71ba80',      #kolejne testy -> task_id
         'ttl': 1750176608
        }
    }

    """
    content_of_task = "make app 2"
    req_body = {
        "content": content_of_task,   # str
        "user_id": "Alamakota",
        "task_id": "mail",
        "is_done": False
    }
    response_put = requests.put(url=ENDPOINT + "/create-task", json=req_body)
    response_body = response_put.json()
    assert response_put.status_code == 200
    assert response_body["task"]["content"] == content_of_task



#get task

def test_create_and_get_task():
    # make task
    req_body = {
        "content": "my_tmp_task_for_get_method",
        "user_id": "Alamakota",
        "task_id": "mail",
        "is_done": False
    }
    response_put = requests.put(url=ENDPOINT + "/create-task", json=req_body)
    assert response_put.status_code == 200

    # extract task_id
    unique_task_id = response_put.json()["task"]["task_id"]

    # test get method
    response = requests.get(url=ENDPOINT + "/get-task/" + unique_task_id)     # https://todo.pixegami.io/get-task/task_unique-task_id
    assert response.status_code == 200
    response_body = response.json()
    assert response_body["is_done"] == False
    assert response_body["content"] == "my_tmp_task_for_get_method"
    assert response_body["user_id"] == "Alamakota"


def test_can_list_tasks():
    """Napisz test który użyje metody do wylistowania zadań
    1. create task
    2. list-tasks (get. /list-tasks/user_id)
    3. assert - crated task is present in response body of point 2.
    """
    req_body = {
        "content": "new",
        "user_id": "Ala213123132132q",
        "task_id": "mail",
        "is_done": False
    }
    response_put = requests.put(url=ENDPOINT + "/create-task", json=req_body)
    assert response_put.status_code == 200
    res = requests.get(url=ENDPOINT + "/list-tasks/" + "Ala213123132132")  # res - odpowiedź
    assert res.status_code == 200
    body = res.json()
    assert len(body["tasks"]) > 0
    # print(res)  #<Response [200]>
    # print(body) #   {"tasks": [{x}, {x2}, {x3}]}
    # len_tasks = len(body["tasks"])
    # print(len_tasks)

def test_can_update_task():
    """
    1. create task
    2. update_task
    3. check if value is updated
    """
    req_body = {
            "content": "old_content",
            "user_id": "Ala12321323123",
            "task_id": "mail",
            "is_done": False
        }
    response_put = requests.put(url=ENDPOINT + "/create-task", json=req_body)
    assert response_put.status_code == 200
    unique_task_id = response_put.json()["task"]["task_id"]
    new_req_body = {
            "content": "new_contentv2",
            "user_id": "Ala12321323123",
            "task_id": unique_task_id,
            "is_done": True
        }

    response_update = requests.put(url=ENDPOINT + "/update-task", json=new_req_body)
    assert response_update.status_code == 200


    response_get = requests.get(url=ENDPOINT + "/get-task/" + unique_task_id)
    body_response_get = response_get.json()
    content = body_response_get["content"]
    # print(content)
    assert content == "new_contentv2"


#aplikacja potrafi tworzyć zadania

# 1) klikasz UI
# 2) api -> put -> ta sama funkcja w kodzie(java)

# prod = 12.1
# test = 12.1 -> 12.2(nowa wersja)   -> ok -> release, prod=12.2



def test_can_delete_task():
    req_body = {
        "content": "new",
        "user_id": "Ala213123132132q",
        "task_id": "mail",
        "is_done": False
    }
    response_put = requests.put(url=ENDPOINT + "/create-task", json=req_body)
    assert response_put.status_code == 200

    unique_task_id = response_put.json()["task"]["task_id"]

    response_get = requests.get(url=ENDPOINT + "/get-task/" + unique_task_id)
    body_response_get = response_get.json()
    assert body_response_get["task_id"] == unique_task_id

    response_delete = requests.delete(url=ENDPOINT + "/delete-task/" + unique_task_id)
    assert response_delete.status_code == 200

    response_get_2 = requests.get(url=ENDPOINT + "/get-task/" + unique_task_id)
    body_response_get_2 = response_get_2.json()  #{"detail": "xxxxxxxxx"}
    print(body_response_get_2["detail"])
    assert body_response_get_2["detail"] == "Task " + unique_task_id + " not found"
