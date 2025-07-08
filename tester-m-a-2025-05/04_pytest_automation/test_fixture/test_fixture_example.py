import pytest

@pytest.fixture
def sample_data():
    var = [1, 2, 3]
    var.append(4)
    return var

def test_sum(sample_data):
    """sample_data = [1, 2, 3, 4]"""
    data_sum = sum(sample_data)
    expected = 10
    assert data_sum == expected

def test_min(sample_data):
    data_min = min(sample_data)
    expected = 1
    assert data_min == expected
