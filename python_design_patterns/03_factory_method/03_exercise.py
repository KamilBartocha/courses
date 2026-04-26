# 03_exercise.py - Factory Method (Metoda Fabrykujaca)

from abc import ABC, abstractmethod

# ─── Zadanie 1 ─ Abstrakcyjny produkt i fabryka ───────────────────────────────
# Zaimplementuj hierarchie eksporterow danych.
# Abstrakcja: Exporter z metoda export(data: list[dict]) -> str.
# Konkretne: CSVExporter (csv), JSONExporter (json string),
# TextExporter (linie "key: value").
# Abstrakcyjna fabryka: ReportCreator.create_exporter() -> Exporter.

class Exporter(ABC):
    @abstractmethod
    def export(self, data: list[dict]) -> str: ...

class CSVExporter(Exporter):
    def export(self, data: list[dict]) -> str:
        pass

class JSONExporter(Exporter):
    def export(self, data: list[dict]) -> str:
        pass

class TextExporter(Exporter):
    def export(self, data: list[dict]) -> str:
        pass

class ReportCreator(ABC):
    @abstractmethod
    def create_exporter(self) -> Exporter: ...

    def generate_report(self, data: list[dict]) -> str:
        pass


data = [{"name": "Alice", "score": 95}, {"name": "Bob", "score": 87}]
print(CSVExporter().export(data))   # name,score\nAlice,95\nBob,87


# ─── Zadanie 2 ─ Rejestr fabryk ───────────────────────────────────────────────
# Napisz rejestr parsow (parsers registry).
# Parsery: JSONParser, CSVParser, XMLParser - kazdy ma parse(text: str) -> dict.
# Funkcja get_parser(fmt: str) -> Parser pobiera z rejestru.
# Rzuc ValueError gdy format nieznany.

class Parser(ABC):
    @abstractmethod
    def parse(self, text: str) -> dict: ...

class JSONParser(Parser):
    def parse(self, text: str) -> dict:
        pass

class CSVParser(Parser):
    def parse(self, text: str) -> dict:
        pass

PARSER_REGISTRY: dict[str, type[Parser]] = {}

def get_parser(fmt: str) -> Parser:
    pass


print(type(get_parser("json")))  # <class 'JSONParser'>
print(type(get_parser("csv")))   # <class 'CSVParser'>


# ─── Zadanie 3 ─ @classmethod jako fabryka ────────────────────────────────────
# Napisz klase User z polami name, email, role.
# Dodaj fabryki: from_dict(d), from_string("name:email:role"),
# guest() tworzaca uzytkownika goscia.

class User:
    def __init__(self, name: str, email: str, role: str = "user"):
        self.name = name
        self.email = email
        self.role = role

    @classmethod
    def from_dict(cls, d: dict) -> "User":
        pass

    @classmethod
    def from_string(cls, s: str) -> "User":
        pass

    @classmethod
    def guest(cls) -> "User":
        pass

    def __repr__(self) -> str:
        return f"User({self.name}, {self.email}, {self.role})"


print(User.from_dict({"name": "Alice", "email": "a@x.com", "role": "admin"}))
print(User.from_string("Bob:b@x.com:editor"))
print(User.guest())  # User(Guest, guest@example.com, guest)


# ─── Zadanie 4 ─ Factory Method z logger ──────────────────────────────────────
# Napisz LoggerFactory.create_logger(level: str) -> Logger.
# Poziomy: "debug", "info", "error" - kazdy wypisuje z prefiksem.
# Rzuc ValueError dla nieznanego poziomu.

class Logger(ABC):
    @abstractmethod
    def log(self, msg: str) -> None: ...

class DebugLogger(Logger):
    def log(self, msg: str) -> None: pass

class InfoLogger(Logger):
    def log(self, msg: str) -> None: pass

class ErrorLogger(Logger):
    def log(self, msg: str) -> None: pass

class LoggerFactory:
    @staticmethod
    def create_logger(level: str) -> Logger:
        pass


LoggerFactory.create_logger("debug").log("Starting")   # [DEBUG] Starting
LoggerFactory.create_logger("info").log("Ready")       # [INFO] Ready
LoggerFactory.create_logger("error").log("Crashed")    # [ERROR] Crashed


# ─── Zadanie 5 ─ Rejestr z automatyczna rejestracja *(Trudniejsze)* ───────────
# Zaimplementuj dekorator @register_plugin(name) rejestrujacy klasy pluginow.
# Pluginy implementuja interfejs Plugin z metoda run() -> str.
# Funkcja get_plugin(name) pobiera z rejestru i tworzy instancje.
# # hint: uzyj slownika na poziomie modulu i domkniecia w dekoratorze

PLUGIN_REGISTRY: dict[str, type] = {}

def register_plugin(name: str):
    pass

class Plugin(ABC):
    @abstractmethod
    def run(self) -> str: ...

@register_plugin("greeter")
class GreeterPlugin(Plugin):
    def run(self) -> str: return "Hello from Greeter!"

@register_plugin("timer")
class TimerPlugin(Plugin):
    def run(self) -> str: return "Timer started!"

def get_plugin(name: str) -> Plugin:
    pass


print(get_plugin("greeter").run())  # Hello from Greeter!
print(get_plugin("timer").run())    # Timer started!
