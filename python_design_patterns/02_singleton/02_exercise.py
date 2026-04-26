# 02_exercise.py - Singleton

import threading

# ─── Zadanie 1 ─ Implementacja naiwna ─────────────────────────────────────────
# Zaimplementuj klase AppLogger jako Singleton uzywajac __new__.
# Klasa powinna miec atrybut instancji `name` (ustawiony w __init__)
# i metode `log(message)` drukujaca "[name] message".

class AppLogger:
    _instance = None

    def __new__(cls, name: str = "App"):
        pass

    def __init__(self, name: str = "App"):
        pass

    def log(self, message: str) -> None:
        pass


logger1 = AppLogger("MyApp")
logger2 = AppLogger()
print(logger1 is logger2)       # True
logger1.log("Started")          # [MyApp] Started
logger2.log("Running")          # [MyApp] Running


# ─── Zadanie 2 ─ Singleton bezpieczny watkowo ─────────────────────────────────
# Zaimplementuj ThreadSafeCounter jako Singleton z licznikiem.
# Metoda increment() zwieksza licznik o 1, count zwraca aktualna wartosc.
# Uzyj threading.Lock do zabezpieczenia przed wycigiem.

class ThreadSafeCounter:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        pass

    def __init__(self):
        pass

    def increment(self) -> None:
        pass

    @property
    def count(self) -> int:
        pass


c1 = ThreadSafeCounter()
c2 = ThreadSafeCounter()
c1.increment()
c1.increment()
c2.increment()
print(c1 is c2)    # True
print(c1.count)    # 3


# ─── Zadanie 3 ─ Wzorzec Borg ─────────────────────────────────────────────────
# Zaimplementuj SharedConfig uzywajac wzorca Borg.
# Klasa powinna przechowywac slownik settings.
# Metody: set(key, value), get(key).

class SharedConfig:
    _shared_state: dict = {}

    def __init__(self):
        pass

    def set(self, key: str, value) -> None:
        pass

    def get(self, key: str):
        pass


cfg1 = SharedConfig()
cfg2 = SharedConfig()
cfg1.set("theme", "dark")
print(cfg2.get("theme"))   # dark
print(cfg1 is cfg2)        # False


# ─── Zadanie 4 ─ Singleton jako dekorator ────────────────────────────────────
# Napisz dekorator singleton(cls) zamieniajacy dowolna klase w Singleton.
# Zastosuj go do klasy DatabaseConnection z atrybutem url.

def singleton(cls):
    pass

@singleton
class DatabaseConnection:
    def __init__(self, url: str = "sqlite:///default.db"):
        self.url = url


db1 = DatabaseConnection("postgres://localhost/mydb")
db2 = DatabaseConnection()
print(db1 is db2)    # True
print(db1.url)       # postgres://localhost/mydb


# ─── Zadanie 5 ─ Reset Singletona w testach *(Trudniejsze)* ──────────────────
# Zaimplementuj TestableSingleton z metoda klasy _reset_instance().
# Napisz prosty test (bez frameworka): sprawdz tozsamosc, zresetuj,
# sprawdz czy nowa instancja jest inna.
# # hint: przechowaj stary id(), wywolaj _reset_instance(), stworz nowy

class TestableSingleton:
    _instance = None

    def __new__(cls):
        pass

    @classmethod
    def _reset_instance(cls) -> None:
        pass


s1 = TestableSingleton()
old_id = id(s1)
TestableSingleton._reset_instance()
s2 = TestableSingleton()
print(s1 is s2)        # False (po resecie)
print(id(s2) != old_id)  # True
