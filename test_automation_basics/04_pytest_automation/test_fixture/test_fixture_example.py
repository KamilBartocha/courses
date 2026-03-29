import os
from time import sleep
import pytest


@pytest.fixture
def sample_data():
    var = [1, 2, 3]
    var.append(44)
    return var  # [1, 2, 3, 4]


def test_sum(sample_data):
    """sample_data = [1, 2, 3, 4]"""
    data_sum = sum(sample_data)
    expected = 50
    print(sample_data)
    assert data_sum == expected


def test_min(sample_data):
    data_min = min(sample_data)
    expected = 1
    print(sample_data)
    assert data_min == expected


@pytest.fixture
def data():
    user = {"name": "John"}
    return user


def test_modify_user(data):
    data["name"] = "Alice"
    assert data["name"] == "Alice"


def test_user_is_John(data):
    assert data["name"] == "John"  # data is not changed


@pytest.fixture
def temp_file():
    """
    lines before yield f -> setup
    lines after  yield f -> teardown

    """
    f = open("test.txt", "w")
    yield f  # return f
    f.close()
    os.remove("test.txt")


def test_file_append(temp_file):
    # przed zrobi plik bo fixture
    temp_file.write("New line\n")
    sleep(10)
    # na samym końcu zamknie plik bo fixture
