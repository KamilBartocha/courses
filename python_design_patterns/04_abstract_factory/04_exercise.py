# 04_exercise.py - Abstract Factory (Fabryka Abstrakcyjna)

from abc import ABC, abstractmethod

# ─── Zadanie 1 ─ Abstrakcyjne produkty ────────────────────────────────────────
# Zaimplementuj rodzine produktow dla systemu baz danych.
# Abstrakcje: Connection (connect() -> str), Query (execute(sql: str) -> str),
# Transaction (commit() -> str, rollback() -> str).
# Konkretne: SQLite* i Postgres* implementujace powyzsze.

class Connection(ABC):
    @abstractmethod
    def connect(self) -> str: ...

class Query(ABC):
    @abstractmethod
    def execute(self, sql: str) -> str: ...

class Transaction(ABC):
    @abstractmethod
    def commit(self) -> str: ...
    @abstractmethod
    def rollback(self) -> str: ...

class SQLiteConnection(Connection):
    def connect(self) -> str: pass

class SQLiteQuery(Query):
    def execute(self, sql: str) -> str: pass

class SQLiteTransaction(Transaction):
    def commit(self) -> str: pass
    def rollback(self) -> str: pass

class PostgresConnection(Connection):
    def connect(self) -> str: pass

class PostgresQuery(Query):
    def execute(self, sql: str) -> str: pass

class PostgresTransaction(Transaction):
    def commit(self) -> str: pass
    def rollback(self) -> str: pass


print(SQLiteConnection().connect())   # Connected to SQLite
print(PostgresConnection().connect()) # Connected to Postgres


# ─── Zadanie 2 ─ Abstrakcyjna fabryka ─────────────────────────────────────────
# Napisz abstrakcyjna fabryke DatabaseFactory z metodami:
# create_connection, create_query, create_transaction.
# Konkretne fabryki: SQLiteFactory, PostgresFactory.

class DatabaseFactory(ABC):
    @abstractmethod
    def create_connection(self) -> Connection: ...
    @abstractmethod
    def create_query(self) -> Query: ...
    @abstractmethod
    def create_transaction(self) -> Transaction: ...

class SQLiteFactory(DatabaseFactory):
    def create_connection(self) -> Connection: pass
    def create_query(self) -> Query: pass
    def create_transaction(self) -> Transaction: pass

class PostgresFactory(DatabaseFactory):
    def create_connection(self) -> Connection: pass
    def create_query(self) -> Query: pass
    def create_transaction(self) -> Transaction: pass


sqlite = SQLiteFactory()
print(sqlite.create_connection().connect())   # Connected to SQLite


# ─── Zadanie 3 ─ Klient uzywajacy fabryki ────────────────────────────────────
# Napisz funkcje run_migration(factory: DatabaseFactory, sql: str).
# Funkcja powinna: polaczyc sie, uruchomic zapytanie w transakcji,
# i zatwierdzic lub cofnac w razie bledu.

def run_migration(factory: DatabaseFactory, sql: str) -> None:
    pass


run_migration(SQLiteFactory(), "CREATE TABLE users (id INT)")
run_migration(PostgresFactory(), "ALTER TABLE orders ADD COLUMN status TEXT")


# ─── Zadanie 4 ─ Wybor fabryki z konfiguracji ────────────────────────────────
# Napisz funkcje get_db_factory(db_type: str) -> DatabaseFactory.
# Wspierane typy: "sqlite", "postgres". Rzuc ValueError dla innych.

def get_db_factory(db_type: str) -> DatabaseFactory:
    pass


factory = get_db_factory("sqlite")
print(type(factory).__name__)   # SQLiteFactory

try:
    get_db_factory("oracle")
except ValueError as e:
    print(e)   # Unknown db type: oracle


# ─── Zadanie 5 ─ Rozszerzanie bez modyfikacji *(Trudniejsze)* ─────────────────
# Dodaj trzeci silnik: MySQL (MySQLConnection, MySQLQuery,
# MySQLTransaction, MySQLFactory).
# Upewnij sie, ze funkcja get_db_factory dziala z "mysql" bez
# modyfikowania istniejacych klas.
# # hint: mozna rozszerzyc slownik w get_db_factory lub uzyc rejestru

class MySQLConnection(Connection):
    def connect(self) -> str: pass

class MySQLQuery(Query):
    def execute(self, sql: str) -> str: pass

class MySQLTransaction(Transaction):
    def commit(self) -> str: pass
    def rollback(self) -> str: pass

class MySQLFactory(DatabaseFactory):
    def create_connection(self) -> Connection: pass
    def create_query(self) -> Query: pass
    def create_transaction(self) -> Transaction: pass


factory = get_db_factory("mysql")
print(factory.create_connection().connect())  # Connected to MySQL
