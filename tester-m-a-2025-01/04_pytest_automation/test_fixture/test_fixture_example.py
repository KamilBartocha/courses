import pytest

@pytest.fixture
def get_data():
    return [1, 2, 3, 4, 5]

def test_sum(get_data):
    result = sum(get_data)
    assert result == 15

def test_min(get_data):
    result = min(get_data)
    pytest.CallInfo.duration
    assert result == 1
