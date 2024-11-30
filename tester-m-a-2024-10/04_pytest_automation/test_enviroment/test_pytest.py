def test_api_response():
    respose_code = 200   # symulacja zwrotu z API
    assert respose_code == 200


def test_api_body_not_empty():
    respose_body = {'a', 'b'}   # symulacja zwrotu z API
    assert len(respose_body) != 0


def test_api_body_status_ok():
    respose_body = {'status': 'OK'}   # symulacja zwrotu z API
    assert respose_body['status'] == 'OK'
