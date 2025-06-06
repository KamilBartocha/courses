import requests

class SimpleBooksAPI:
    def __init__(self):
        self.base_url = "https://simple-books-api.glitch.me"

    def get_status(self):
        response = requests.get(f"{self.base_url}/status")
        print(response.json())
        print(response.status_code)
        assert response.status_code == 200

    def get_status_negative(self):
        response = requests.get(f"{self.base_url}/statu")
        print(response.status_code)
        assert response.status_code == 404

if __name__ == "__main__":
    api = SimpleBooksAPI()
    api.get_status()
    api.get_status_negative()
