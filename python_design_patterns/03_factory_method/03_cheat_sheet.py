# 03_cheat_sheet.py - Factory Method (Metoda Fabrykujaca)

from abc import ABC, abstractmethod


# ── Implementacja z abc.ABC ───────────────────────────────────────────────────
class Notification(ABC):
    @abstractmethod
    def send(self, message: str) -> None: ...

class EmailNotification(Notification):
    def send(self, message: str) -> None:
        print(f"Email: {message}")

class SMSNotification(Notification):
    def send(self, message: str) -> None:
        print(f"SMS: {message}")

class PushNotification(Notification):
    def send(self, message: str) -> None:
        print(f"Push: {message}")

class NotificationCreator(ABC):
    @abstractmethod
    def create_notification(self) -> Notification: ...

    def notify(self, message: str) -> None:  # metoda szablonowa
        notif = self.create_notification()
        notif.send(message)

class EmailCreator(NotificationCreator):
    def create_notification(self) -> Notification:
        return EmailNotification()

class SMSCreator(NotificationCreator):
    def create_notification(self) -> Notification:
        return SMSNotification()

creator = EmailCreator()
creator.notify("Hello!")   # Email: Hello!


# ── Rejestr fabryk ────────────────────────────────────────────────────────────
_registry: dict[str, type[Notification]] = {
    "email": EmailNotification,
    "sms": SMSNotification,
    "push": PushNotification,
}

def create_notification(channel: str) -> Notification:
    cls = _registry.get(channel)
    if cls is None:
        raise ValueError(f"Unknown channel: {channel}")
    return cls()

notif = create_notification("email")
notif.send("Registered!")   # Email: Registered!


# ── @classmethod jako fabryka ─────────────────────────────────────────────────
class Connection:
    def __init__(self, host: str, port: int, db: str):
        self.host = host
        self.port = port
        self.db = db

    @classmethod
    def from_url(cls, url: str) -> "Connection":
        # "postgres://localhost:5432/mydb"
        parts = url.replace("://", " ").replace(":", " ").replace("/", " ")
        scheme, host, port, db = parts.split()
        return cls(host, int(port), db)

    @classmethod
    def from_dict(cls, config: dict) -> "Connection":
        return cls(config["host"], config["port"], config["db"])

    def __repr__(self) -> str:
        return f"Connection({self.host}:{self.port}/{self.db})"

conn1 = Connection.from_url("postgres://localhost:5432/mydb")
conn2 = Connection.from_dict({"host": "localhost", "port": 3306, "db": "shop"})
print(conn1)   # Connection(localhost:5432/mydb)
print(conn2)   # Connection(localhost:3306/shop)
