def send_request():
    return 201

def test_api():
    """ wyślij zapytanie i oczekuj kodu 200"""
    actual_value = send_request()
    excepted_value = 200
    # if actual_value == excepted_value:
    #     PASS
    # else:
    #     FAIL
    assert actual_value == excepted_value
