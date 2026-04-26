# 02_cheat_sheet.py - Singleton

import threading


# ── Implementacja naiwna ───────────────────────────────────────────────────────
class SingletonNaive:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

s1 = SingletonNaive()
s2 = SingletonNaive()
print(s1 is s2)   # True
print(id(s1) == id(s2))  # True


# ── Singleton bezpieczny watkowo ──────────────────────────────────────────────
class ThreadSafeSingleton:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:   # double-checked locking
                    cls._instance = super().__new__(cls)
        return cls._instance

    @classmethod
    def _reset(cls):
        cls._instance = None


# ── Wzorzec Borg (monostate) ──────────────────────────────────────────────────
# Rozne instancje, wspoldzielony stan
class BorgSingleton:
    _shared_state: dict = {}

    def __init__(self):
        self.__dict__ = self._shared_state

b1 = BorgSingleton()
b2 = BorgSingleton()
b1.value = 42
print(b2.value)   # 42 - wspoldzielony stan
print(b1 is b2)   # False - rozne instancje


# ── Modul jako Singleton ──────────────────────────────────────────────────────
# config.py - modul jest ladowany raz przez Python
_config = {
    "debug": False,
    "db_url": "sqlite:///app.db",
    "max_connections": 10,
}

def get(key: str):
    return _config[key]

def set(key: str, value) -> None:
    _config[key] = value


# ── Singleton jako dekorator klasy ────────────────────────────────────────────
def singleton(cls):
    instances = {}
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance

@singleton
class AppConfig:
    def __init__(self):
        self.theme = "dark"
        self.language = "pl"

cfg1 = AppConfig()
cfg2 = AppConfig()
print(cfg1 is cfg2)  # True
