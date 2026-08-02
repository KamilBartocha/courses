# 10_cheat_sheet.py - Proxy (Pelnomocnik)

from abc import ABC, abstractmethod
import time


# ── Wspolny interfejs ─────────────────────────────────────────────────────────
class Image(ABC):
    @abstractmethod
    def display(self) -> None: ...

class RealImage(Image):
    def __init__(self, filename: str):
        self.filename = filename
        self._load()

    def _load(self) -> None:
        print(f'Loading image from disk: {self.filename}')
        time.sleep(0.01)  # symulacja I/O

    def display(self) -> None:
        print(f'Displaying: {self.filename}')


# ── Proxy wirtualne (lazy loading) ───────────────────────────────────────────
class LazyImageProxy(Image):
    def __init__(self, filename: str):
        self.filename = filename
        self._real: RealImage | None = None

    def display(self) -> None:
        if self._real is None:           # laduje tylko gdy potrzebne
            self._real = RealImage(self.filename)
        self._real.display()

proxy = LazyImageProxy('photo.jpg')
print('Proxy created (no loading yet)')
proxy.display()   # Loading + Displaying
proxy.display()   # tylko Displaying (juz zaladowane)


# ── Proxy ochronne (access control) ─────────────────────────────────────────
class DatabaseService:
    def read(self, sql: str) -> list:
        return [{'id': 1, 'name': 'Alice'}]
    def write(self, sql: str) -> None:
        print(f'Executing: {sql}')

class ProtectionProxy(DatabaseService):
    def __init__(self, service: DatabaseService, read_only: bool):
        self._service = service
        self._read_only = read_only

    def read(self, sql: str) -> list:
        return self._service.read(sql)

    def write(self, sql: str) -> None:
        if self._read_only:
            raise PermissionError('Read-only mode: write not allowed')
        self._service.write(sql)

db = ProtectionProxy(DatabaseService(), read_only=True)
print(db.read('SELECT * FROM users'))
try:
    db.write('DELETE FROM users')
except PermissionError as e:
    print(e)


# ── Proxy cache'ujace ─────────────────────────────────────────────────────────
class ExpensiveAPI:
    def fetch(self, endpoint: str) -> dict:
        print(f'Network request: {endpoint}')
        time.sleep(0.01)
        return {'endpoint': endpoint, 'data': [1, 2, 3]}

class CachingProxy(ExpensiveAPI):
    def __init__(self, api: ExpensiveAPI):
        self._api = api
        self._cache: dict = {}

    def fetch(self, endpoint: str) -> dict:
        if endpoint not in self._cache:
            self._cache[endpoint] = self._api.fetch(endpoint)
        else:
            print(f'Cache hit: {endpoint}')
        return self._cache[endpoint]

api = CachingProxy(ExpensiveAPI())
api.fetch('/users')    # Network request
api.fetch('/users')    # Cache hit
api.fetch('/products') # Network request


# ── __getattr__ jako proxy dynamiczne ────────────────────────────────────────
class LoggingProxy:
    def __init__(self, target):
        object.__setattr__(self, '_target', target)

    def __getattr__(self, name: str):
        attr = getattr(object.__getattribute__(self, '_target'), name)
        if callable(attr):
            def logged(*args, **kwargs):
                print(f'CALL: {name}({args}, {kwargs})')
                result = attr(*args, **kwargs)
                print(f'RETURN: {result}')
                return result
            return logged
        return attr

class Calculator:
    def add(self, a: int, b: int) -> int: return a + b
    def multiply(self, a: int, b: int) -> int: return a * b

calc = LoggingProxy(Calculator())
calc.add(3, 4)
calc.multiply(5, 6)
