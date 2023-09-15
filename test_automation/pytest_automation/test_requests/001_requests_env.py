import requests


url = 'https://simple-books-api.glitch.me/status'

try:
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print("Dane z serwera:", data)
    else:
        print("Błąd HTTP:", response.status_code)
except requests.exceptions.RequestException as e:
    print("Wystąpił błąd podczas wysyłania żądania:", e)
