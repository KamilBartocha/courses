import requests
response_get = requests.get("https://todo.pixegami.io")
print(response_get)    # <Response [200]>
print(response_get.status_code)   # int
print(response_get.json())        # dict
print(response_get.json()["message"])        # dict
body = response_get.json()  #-> body: {'message': 'Hello World from Todo API'}
print(body["message"])

import random
print(random.randint(1000000, 9999999))


# def test_can_call_api():
#     response = requests.get("https://todo.pixegami.io")
#     code = response.status_code
#     expected = 200
#     print(f"expected: {expected}, status_code: {code}")
#     assert code == expected







"""
{'tasks':
[
 {'is_done': False, 'content': 'Nakarm kota', 'ttl': 1752398663, 'user_id': 'Alamakota_tmp', 'task_id': 'task_637ab49d11614b3a93d05791deef12af', 'created_time': 1752312263},
 {'is_done': False, 'content': 'Nakarm kota', 'ttl': 1752398593, 'user_id': 'Alamakota_tmp', 'task_id': 'task_90303a378bd54565a4ce76fd3bedf83d', 'created_time': 1752312193},
 {'is_done': False, 'content': 'Nakarm kota', 'ttl': 1752398473, 'user_id': 'Alamakota_tmp', 'task_id': 'task_d5e08dfd49b14e759224bc683072584b', 'created_time': 1752312073},
 {'is_done': False, 'content': 'Nakarm kota', 'ttl': 1752398405, 'user_id': 'Alamakota_tmp', 'task_id': 'task_35be08c1ed364dc1869d8b32e5ce7899', 'created_time': 1752312005},
 {'is_done': False, 'content': 'Nakarm kota', 'ttl': 1752398343, 'user_id': 'Alamakota_tmp', 'task_id': 'task_8ff4a179e8c748a2885705ddf4cfaea8', 'created_time': 1752311943},
 {'is_done': False, 'content': 'Nakarm kota', 'ttl': 1752398261, 'user_id': 'Alamakota_tmp', 'task_id': 'task_032fa8fa8d27421f9f46f48ce73048ea', 'created_time': 1752311861},
 {'is_done': False, 'content': 'Nakarm kota', 'ttl': 1752398216, 'user_id': 'Alamakota_tmp', 'task_id': 'task_c6dfcfc447f947bfa47757cb34710d4e', 'created_time': 1752311816},
 {'is_done': False, 'content': 'Nakarm kota', 'ttl': 1752398186, 'user_id': 'Alamakota_tmp', 'task_id': 'task_637d4830d15e40589455a2543e839dd1', 'created_time': 1752311786},
 {'is_done': False, 'content': 'Nakarm kota', 'ttl': 1752397768, 'user_id': 'Alamakota_tmp', 'task_id': 'task_51623c6ed60a4b99ae02cd76eed163a4', 'created_time': 1752311368},
 {'is_done': False, 'content': 'Nakarm kota', 'ttl': 1752397367, 'user_id': 'Alamakota_tmp', 'task_id': 'task_1fe38b05228249aa8da3505b6175da87', 'created_time': 1752310967}
]
}


{'tasks': []}





"""