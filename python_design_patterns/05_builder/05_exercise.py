# 05_exercise.py - Builder (Budowniczy)

from dataclasses import dataclass, field
from typing import Optional

# ─── Zadanie 1 ─ Prosty Builder ───────────────────────────────────────────────
# Zaimplementuj builder dla klasy Computer.
# Pola: cpu (str), ram_gb (int), storage_gb (int),
#       gpu (str = "integrated"), os (str = "Linux").
# Builder: cpu(), ram(), storage(), gpu(), os(), build() -> Computer.

@dataclass
class Computer:
    cpu: str
    ram_gb: int
    storage_gb: int
    gpu: str = "integrated"
    os: str = "Linux"

    def __repr__(self) -> str:
        return (f"Computer(CPU={self.cpu}, RAM={self.ram_gb}GB, "
                f"SSD={self.storage_gb}GB, GPU={self.gpu}, OS={self.os})")

class ComputerBuilder:
    def cpu(self, cpu: str) -> "ComputerBuilder":
        pass

    def ram(self, gb: int) -> "ComputerBuilder":
        pass

    def storage(self, gb: int) -> "ComputerBuilder":
        pass

    def gpu(self, gpu: str) -> "ComputerBuilder":
        pass

    def os(self, os: str) -> "ComputerBuilder":
        pass

    def build(self) -> Computer:
        pass


pc = (ComputerBuilder()
      .cpu("Intel i9")
      .ram(32)
      .storage(1000)
      .gpu("RTX 4090")
      .os("Windows 11")
      .build())
print(pc)  # Computer(CPU=Intel i9, RAM=32GB, SSD=1000GB, GPU=RTX 4090, OS=Windows 11)


# ─── Zadanie 2 ─ Builder z walidacja ─────────────────────────────────────────
# Zaimplementuj EmailBuilder.
# Pola: sender (str), recipients (list[str]), subject (str),
#       body (str), attachments (list[str] = []).
# Metoda build() rzuca ValueError jesli sender, subject lub body sa puste
# lub lista recipients jest pusta.

@dataclass
class Email:
    sender: str
    recipients: list[str]
    subject: str
    body: str
    attachments: list[str] = field(default_factory=list)

class EmailBuilder:
    def sender(self, email: str) -> "EmailBuilder":
        pass

    def to(self, *recipients: str) -> "EmailBuilder":
        pass

    def subject(self, subject: str) -> "EmailBuilder":
        pass

    def body(self, body: str) -> "EmailBuilder":
        pass

    def attach(self, filename: str) -> "EmailBuilder":
        pass

    def build(self) -> Email:
        pass


email = (EmailBuilder()
         .sender("alice@example.com")
         .to("bob@example.com", "carol@example.com")
         .subject("Meeting tomorrow")
         .body("Hi all, meeting at 10am.")
         .build())
print(email.sender, "->", email.recipients)  # alice@example.com -> [...]

try:
    EmailBuilder().build()
except ValueError as e:
    print(e)  # Sender is required


# ─── Zadanie 3 ─ Fluent SQL Builder ──────────────────────────────────────────
# Napisz InsertBuilder generujacy zapytanie INSERT INTO.
# Metody: into(table), value(column, val), build() -> str.
# Wynik: "INSERT INTO table (col1, col2) VALUES (val1, val2)"

class InsertBuilder:
    def into(self, table: str) -> "InsertBuilder":
        pass

    def value(self, column: str, val) -> "InsertBuilder":
        pass

    def build(self) -> str:
        pass


sql = (InsertBuilder()
       .into("users")
       .value("name", "Alice")
       .value("age", 30)
       .value("active", True)
       .build())
print(sql)  # INSERT INTO users (name, age, active) VALUES (Alice, 30, True)


# ─── Zadanie 4 ─ Dyrektor ────────────────────────────────────────────────────
# Napisz ComputerDirector z metodami:
# make_office_pc(builder) i make_gaming_pc(builder).
# Office: cpu="Intel i5", ram=16, storage=256, os="Windows 11"
# Gaming: cpu="AMD Ryzen 9", ram=32, storage=2000, gpu="RTX 4080", os="Windows 11"

class ComputerDirector:
    @staticmethod
    def make_office_pc(builder: ComputerBuilder) -> Computer:
        pass

    @staticmethod
    def make_gaming_pc(builder: ComputerBuilder) -> Computer:
        pass


office = ComputerDirector.make_office_pc(ComputerBuilder())
gaming = ComputerDirector.make_gaming_pc(ComputerBuilder())
print(office)
print(gaming)


# ─── Zadanie 5 ─ Builder dla HTTP Request *(Trudniejsze)* ────────────────────
# Zaimplementuj HTTPRequestBuilder.
# Pola: method (str = "GET"), url (str), headers (dict), body (str = ""),
#       timeout (int = 30).
# Metody: get(url), post(url), header(k, v), json_body(data: dict),
#         timeout(s), build() -> dict.
# build() rzuca ValueError gdy url jest pusty.
# # hint: json_body uzywa json.dumps() i dodaje Content-Type header

import json

@dataclass
class HTTPRequest:
    method: str
    url: str
    headers: dict
    body: str
    timeout: int

class HTTPRequestBuilder:
    def get(self, url: str) -> "HTTPRequestBuilder": pass
    def post(self, url: str) -> "HTTPRequestBuilder": pass
    def header(self, key: str, value: str) -> "HTTPRequestBuilder": pass
    def json_body(self, data: dict) -> "HTTPRequestBuilder": pass
    def timeout(self, seconds: int) -> "HTTPRequestBuilder": pass
    def build(self) -> HTTPRequest: pass


req = (HTTPRequestBuilder()
       .post("https://api.example.com/users")
       .header("Authorization", "Bearer token123")
       .json_body({"name": "Alice", "role": "admin"})
       .timeout(60)
       .build())
print(req.method, req.url)       # POST https://api.example.com/users
print(req.headers)               # {..., "Content-Type": "application/json"}
print(req.timeout)               # 60
