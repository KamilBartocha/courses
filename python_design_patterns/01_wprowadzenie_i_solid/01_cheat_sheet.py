# 01_cheat_sheet.py - Wprowadzenie i zasady SOLID

# ── Wzorce projektowe ─────────────────────────────────────────────────────────
# Wzorzec projektowy (design pattern) to sprawdzone rozwiązanie
# powtarzajacego sie problemu projektowego.

# Trzy kategorie (GoF):
#   kreacyjne   (creational)  - tworzenie obiektow
#   strukturalne (structural) - skladanie obiektow
#   behawioralne (behavioral) - komunikacja obiektow


# ── SOLID: Single Responsibility Principle ────────────────────────────────────
# ZLE: klasa robi za duzo
class BadOrder:
    def calculate_total(self): pass
    def save_to_db(self): pass      # nie jej odpowiedzialnosc
    def send_email(self): pass      # nie jej odpowiedzialnosc

# DOBRZE: kazda klasa ma jeden powod do zmiany
class Order:
    def calculate_total(self): pass

class OrderRepository:
    def save(self, order): pass

class EmailService:
    def send_confirmation(self, order): pass


# ── SOLID: Open/Closed Principle ──────────────────────────────────────────────
from abc import ABC, abstractmethod

class Discount(ABC):
    @abstractmethod
    def apply(self, price: float) -> float: ...

class PercentDiscount(Discount):
    def __init__(self, pct: float): self.pct = pct
    def apply(self, price: float) -> float: return price * (1 - self.pct)

class FixedDiscount(Discount):
    def __init__(self, amount: float): self.amount = amount
    def apply(self, price: float) -> float: return price - self.amount

# Dodajemy nowy typ rabatu bez modyfikacji istniejacych klas:
class SeasonalDiscount(Discount):
    def apply(self, price: float) -> float: return price * 0.85


# ── SOLID: Liskov Substitution Principle ─────────────────────────────────────
class Shape(ABC):
    @abstractmethod
    def area(self) -> float: ...

class Rectangle(Shape):
    def __init__(self, w: float, h: float): self.w = w; self.h = h
    def area(self) -> float: return self.w * self.h

class Square(Shape):
    def __init__(self, side: float): self.side = side
    def area(self) -> float: return self.side ** 2

def print_area(shape: Shape) -> None:
    print(f"Area: {shape.area()}")

print_area(Rectangle(3, 4))  # Area: 12
print_area(Square(5))        # Area: 25


# ── SOLID: Interface Segregation Principle ────────────────────────────────────
class Printable(ABC):
    @abstractmethod
    def print_doc(self): ...

class Scannable(ABC):
    @abstractmethod
    def scan(self): ...

class Faxable(ABC):
    @abstractmethod
    def fax(self): ...

class BasicPrinter(Printable):
    def print_doc(self): print("Printing...")

class MultifunctionPrinter(Printable, Scannable, Faxable):
    def print_doc(self): print("Printing...")
    def scan(self): print("Scanning...")
    def fax(self): print("Faxing...")


# ── SOLID: Dependency Inversion Principle ─────────────────────────────────────
class Logger(ABC):
    @abstractmethod
    def log(self, message: str): ...

class ConsoleLogger(Logger):
    def log(self, message: str): print(f"LOG: {message}")

class FileLogger(Logger):
    def log(self, message: str): open("app.log", "a").write(message + "\n")

class UserService:
    def __init__(self, logger: Logger):    # zaleznosc od abstrakcji
        self._logger = logger

    def create_user(self, name: str):
        self._logger.log(f"Creating user: {name}")

service = UserService(ConsoleLogger())
service.create_user("Alice")


# ── typing.Protocol - duck typing ─────────────────────────────────────────────
from typing import Protocol

class Drawable(Protocol):
    def draw(self) -> None: ...

class Circle:
    def draw(self) -> None: print("Drawing circle")

class Triangle:
    def draw(self) -> None: print("Drawing triangle")

def render(shape: Drawable) -> None:
    shape.draw()

render(Circle())    # OK - Circle ma metode draw
render(Triangle())  # OK - Triangle ma metode draw
