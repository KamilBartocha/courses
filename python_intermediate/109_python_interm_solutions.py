### 2

class ReadOnlyFile:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self.file = open(self.filename, "r")
        return self

    def write(self, *args, **kwargs):
        raise IOError("File is read-only. Writing is not allowed.")

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()

    def read(self):
        return self.file.read()



with ReadOnlyFile("example.txt") as file:
    print(file.read())
    file.write("Hello!")



#### 3
import requests

class APIConnection:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = None

    def __enter__(self):
        self.session = requests.Session()
        self.session.headers.update({"User-Agent": "APIConnection/1.0"})
        return self

    def get(self, endpoint, params=None):
        response = self.session.get(self.base_url + endpoint, params=params)
        response.raise_for_status()
        return response.json()

    def post(self, endpoint, data=None, json=None):
        response = self.session.post(self.base_url + endpoint, data=data, json=json)
        response.raise_for_status()
        return response.json()

    def __exit__(self, exc_type, exc_value, traceback):
        self.session.close()


with APIConnection("https://jsonplaceholder.typicode.com") as api:
    users = api.get("/users")
    print(users[0])


#---------------------- @contextmanager --------------------------------------#
import requests
from contextlib import contextmanager

@contextmanager
def api_connection(base_url):
    session = requests.Session()
    session.headers.update({"User-Agent": "APIConnection/1.0"})

    try:
        yield session
    finally:
        session.close()