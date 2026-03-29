import pytest
import os

# 1) fixture vs dane globalnie:
@pytest.fixture
def user():
    user = {"name": "John"}
    return user

def test_modify_user(user):
    user["name"] = "Alice"
    assert user["name"] == "Alice"


def test_user_is_John(user):
    assert user["name"] == "John"    #Fresh data from fixture for every test!















user = {"name": "John"}

def test_modify_user():
    user["name"] = "Alice"
    assert user["name"] == "Alice"

def test_user_is_John():
    assert user["name"] == "John"  # data is changed (muttable object)


# 2) setup i teardown

# setup
#   test
# teardown

@pytest.fixture
def temp_file():
    """
    lines before yield f -> setup
    lines after  yield f -> teardown

    """
    f = open("test.txt", "w")
    yield f   # return f
    f.close()
    os.remove("test.txt")


def test_file_append(temp_file):
    with open(temp_file, "a") as f:
        f.write("New line\n")

    with open(temp_file, "r") as f:
        content = f.read()

    assert "New line" in content


