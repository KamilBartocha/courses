# 01_exercise.py - Wprowadzenie i zasady SOLID

# ─── Zadanie 1 ─ Single Responsibility Principle ──────────────────────────────
# Klasa Invoice ponizej narusza SRP. Podziel ja na trzy klasy:
# Invoice, InvoiceRepository, InvoicePrinter.

class Invoice:
    def __init__(self, items: list[dict]):
        self.items = items

    def calculate_total(self) -> float:
        """Return sum of all item prices."""
        pass

    def save_to_file(self, filename: str) -> None:
        """Save invoice data to a text file."""
        pass

    def print_invoice(self) -> None:
        """Print invoice to stdout."""
        pass


items = [{"name": "Widget", "price": 10.0}, {"name": "Gadget", "price": 25.0}]
invoice = Invoice(items)
print(invoice.calculate_total())  # 35.0


# ─── Zadanie 2 ─ Open/Closed Principle ────────────────────────────────────────
# Zaimplementuj hierarchie rabatow (Discount). Nie modyfikuj istniejacych klas.
# Dodaj NoDiscount, PercentDiscount(pct), FixedDiscount(amount).

from abc import ABC, abstractmethod

class Discount(ABC):
    @abstractmethod
    def apply(self, price: float) -> float:
        """Apply discount to price and return new price."""
        ...

class NoDiscount(Discount):
    def apply(self, price: float) -> float:
        pass

class PercentDiscount(Discount):
    def __init__(self, pct: float):
        self.pct = pct

    def apply(self, price: float) -> float:
        pass

class FixedDiscount(Discount):
    def __init__(self, amount: float):
        self.amount = amount

    def apply(self, price: float) -> float:
        pass


price = 100.0
print(NoDiscount().apply(price))          # 100.0
print(PercentDiscount(0.2).apply(price))  # 80.0
print(FixedDiscount(15.0).apply(price))   # 85.0


# ─── Zadanie 3 ─ Dependency Inversion Principle ───────────────────────────────
# Napisz klase NotificationService zalejna od abstrakcji Notifier.
# Zaimplementuj EmailNotifier i SMSNotifier.

class Notifier(ABC):
    @abstractmethod
    def send(self, message: str) -> None:
        """Send a notification message."""
        ...

class EmailNotifier(Notifier):
    def send(self, message: str) -> None:
        pass

class SMSNotifier(Notifier):
    def send(self, message: str) -> None:
        pass

class NotificationService:
    def __init__(self, notifier: Notifier):
        pass

    def notify(self, message: str) -> None:
        """Send notification using the injected notifier."""
        pass


service_email = NotificationService(EmailNotifier())
service_sms = NotificationService(SMSNotifier())
service_email.notify("Order confirmed")   # Email: Order confirmed
service_sms.notify("Package shipped")     # SMS: Package shipped


# ─── Zadanie 4 ─ typing.Protocol ─────────────────────────────────────────────
# Napisz protokol Serializable z metodami serialize() -> str i
# deserialize(data: str). Napisz JSONSerializer i XMLSerializer.
# Napisz funkcje save(obj: Serializable) drukujaca wynik serialize().

from typing import Protocol

class Serializable(Protocol):
    def serialize(self) -> str: ...

class JSONSerializer:
    def serialize(self) -> str:
        pass

class XMLSerializer:
    def serialize(self) -> str:
        pass

def save(obj: Serializable) -> None:
    pass


save(JSONSerializer())  # {"format": "json"}
save(XMLSerializer())   # <format>xml</format>


# ─── Zadanie 5 ─ Interface Segregation *(Trudniejsze)* ───────────────────────
# Podziel interfejs Animal na mniejsze protokoly:
# Walkable (walk), Swimmable (swim), Flyable (fly).
# Napisz Duck (chodzi, plywa, lata), Dog (chodzi, plywa),
# Eagle (chodzi, lata). Napisz funkcje move(animal) wywolujaca
# wszystkie dostepne metody (sprawdz hasattr).
# # hint: uzyj hasattr(animal, "swim") do sprawdzenia

class Walkable(Protocol):
    def walk(self) -> str: ...

class Swimmable(Protocol):
    def swim(self) -> str: ...

class Flyable(Protocol):
    def fly(self) -> str: ...

class Duck:
    def walk(self) -> str: pass
    def swim(self) -> str: pass
    def fly(self) -> str: pass

class Dog:
    def walk(self) -> str: pass
    def swim(self) -> str: pass

class Eagle:
    def walk(self) -> str: pass
    def fly(self) -> str: pass

def move(animal) -> None:
    pass


move(Duck())   # Walking, Swimming, Flying
move(Dog())    # Walking, Swimming
move(Eagle())  # Walking, Flying
