import pytest


@pytest.fixture
def sample_data():
    """Przykładowa fixture zwracająca listę danych"""
    return [1, 2, 3, 4, 5]

def test_sum(sample_data):
    """Przykładowy test 1 korzystający z fixture 'sample_data'"""
    result = sum(sample_data)
    assert result == 15

def test_min(sample_data):
    """Przykładowy test 2 korzystający z fixture 'sample_data'"""
    result = min(sample_data)
    assert result == 1

def test_max(sample_data):
    """Przykładowy test 3 korzystający z fixture 'sample_data'"""
    result = max(sample_data)
    assert result == 5