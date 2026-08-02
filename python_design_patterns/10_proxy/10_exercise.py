# 10_exercise.py - Proxy (Pelnomocnik)

from abc import ABC, abstractmethod
import time

# ─── Zadanie 1 ─ Proxy wirtualne (lazy loading) ───────────────────────────────
# LargeReport.generate() generuje raport (drogi w czasie).
# Napisz LazyReportProxy z ta sama metoda generate().
# Tworzenie raportu powinno odbyc sie tylko przy pierwszym wywolaniu.

class LargeReport:
    def __init__(self, name: str):
        self.name = name
        print(f'Generating report: {name}...')  # drogie
        self._data = list(range(1000))

    def generate(self) -> str:
        return f'Report({self.name}, {len(self._data)} rows)'

class LazyReportProxy:
    def __init__(self, name: str):
        self._name = name
        self._report = None

    def generate(self) -> str:
        pass


proxy = LazyReportProxy('annual_sales')
print('Proxy created (no generation yet)')
print(proxy.generate())  # generuje teraz
print(proxy.generate())  # bez ponownego generowania


# ─── Zadanie 2 ─ Proxy ochronne ───────────────────────────────────────────────
# UserService.get_users() -> list, create_user(name) -> dict,
# delete_user(id) -> None.
# Napisz AccessControlProxy(service, role: str).
# 'admin' moze wszystko, 'viewer' tylko get_users().

class UserService:
    def get_users(self) -> list:
        return [{'id': 1, 'name': 'Alice'}]
    def create_user(self, name: str) -> dict:
        print(f'Creating user: {name}')
        return {'id': 2, 'name': name}
    def delete_user(self, user_id: int) -> None:
        print(f'Deleting user: {user_id}')

class AccessControlProxy:
    def __init__(self, service: UserService, role: str):
        pass

    def get_users(self) -> list:
        pass

    def create_user(self, name: str) -> dict:
        pass

    def delete_user(self, user_id: int) -> None:
        pass


admin_proxy = AccessControlProxy(UserService(), 'admin')
viewer_proxy = AccessControlProxy(UserService(), 'viewer')

print(admin_proxy.get_users())
admin_proxy.create_user('Bob')
admin_proxy.delete_user(1)

print(viewer_proxy.get_users())
try:
    viewer_proxy.create_user('Eve')
except PermissionError as e:
    print(f'Permission: {e}')


# ─── Zadanie 3 ─ Proxy cache'ujące ────────────────────────────────────────────
# WeatherAPI.get_weather(city: str) -> dict (symuluj opoznienie 0.05s).
# Napisz CachedWeatherProxy z TTL (time-to-live) = 60 sekund.
# Jesli dane sa wieksze niz TTL - pobierz ponownie.

class WeatherAPI:
    def get_weather(self, city: str) -> dict:
        time.sleep(0.01)  # symulacja sieci
        return {'city': city, 'temp': 20, 'condition': 'sunny'}

class CachedWeatherProxy:
    TTL = 60  # sekund

    def __init__(self, api: WeatherAPI):
        self._api = api
        self._cache: dict[str, tuple] = {}  # {city: (data, timestamp)}

    def get_weather(self, city: str) -> dict:
        pass  # sprawdz TTL, pobierz jesli wygaslo


proxy = CachedWeatherProxy(WeatherAPI())
result1 = proxy.get_weather('Warsaw')
result2 = proxy.get_weather('Warsaw')  # powinien uzyc cache
result3 = proxy.get_weather('Krakow')  # nowe zapytanie
print(f'Warsaw: {result1}')
print(f'Warsaw (cached): {result2}')
print(f'Krakow: {result3}')


# ─── Zadanie 4 ─ Proxy logujace przez __getattr__ ────────────────────────────
# Napisz LoggingProxy(target) loggujace kazde wywolanie metody.
# Format: "CALL: method_name(args) -> result"

class LoggingProxy:
    def __init__(self, target):
        pass

    def __getattr__(self, name: str):
        pass


class StringProcessor:
    def upper(self, text: str) -> str: return text.upper()
    def reverse(self, text: str) -> str: return text[::-1]
    def word_count(self, text: str) -> int: return len(text.split())

proc = LoggingProxy(StringProcessor())
proc.upper('hello world')
proc.reverse('Python')
proc.word_count('design patterns are cool')


# ─── Zadanie 5 ─ Proxy kompozytowe *(Trudniejsze)* ───────────────────────────
# Napisz CompositeProxy(service, proxies: list) stosujacy wiele
# proxy kolejno (lazy loading + cache + logging + access control).
# # hint: zamiast dziedziczenia, uzyj lancucha proxy (jeden owija drugi)

class DataService:
    def fetch(self, query: str) -> list:
        print(f'Fetching: {query}')
        return [{'query': query, 'result': [1, 2, 3]}]

class CachingDataProxy:
    def __init__(self, service):
        self._service = service
        self._cache = {}
    def fetch(self, query: str) -> list:
        if query not in self._cache:
            self._cache[query] = self._service.fetch(query)
        else:
            print(f'[Cache] Hit: {query}')
        return self._cache[query]

class LoggingDataProxy:
    def __init__(self, service):
        self._service = service
    def fetch(self, query: str) -> list:
        print(f'[Log] Fetching: {query}')
        result = self._service.fetch(query)
        print(f'[Log] Got {len(result)} results')
        return result

# Uzyj lancucha: LoggingProxy -> CachingProxy -> DataService
service = DataService()
cached = CachingDataProxy(service)
logged_and_cached = LoggingDataProxy(cached)

logged_and_cached.fetch('SELECT * FROM products')
print('---')
logged_and_cached.fetch('SELECT * FROM products')  # cache hit
