import requests

def send_request(ENDPOINT):
    return requests.get(url=ENDPOINT)

def create_task(ENDPOINT, payload):
    return requests.put(url=ENDPOINT + "create-task", json=payload)

def update_task(ENDPOINT, new_payload):
    return requests.put(url=ENDPOINT + "update-task", json=new_payload)

def get_task(ENDPOINT, task_id):
    return requests.get(ENDPOINT + "get-task/" + task_id)

def delete_task(ENDPOINT, task_id):
    return requests.delete(url=ENDPOINT + "delete-task/" + task_id)
