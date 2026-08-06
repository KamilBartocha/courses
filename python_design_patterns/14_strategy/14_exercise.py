# 14_exercise.py - Strategy (Strategia)

from abc import ABC, abstractmethod
from typing import Callable

# ─── Zadanie 1 ─ Kompresja danych ─────────────────────────────────────────────
# CompressionStrategy.compress(data: bytes) -> bytes
# ZipCompression, GzipCompression, NoCompression
# FileCompressor(strategy).compress_file(path)

class CompressionStrategy(ABC):
    @abstractmethod
    def compress(self, data: bytes) -> bytes: ...
    @abstractmethod
    def name(self) -> str: ...

class ZipCompression(CompressionStrategy):
    def compress(self, data: bytes) -> bytes:
        import zlib
        return zlib.compress(data)
    def name(self) -> str: return 'zip'

class GzipCompression(CompressionStrategy):
    def compress(self, data: bytes) -> bytes:
        import gzip
        return gzip.compress(data)
    def name(self) -> str: return 'gzip'

class NoCompression(CompressionStrategy):
    def compress(self, data: bytes) -> bytes: return data
    def name(self) -> str: return 'none'

class FileCompressor:
    def __init__(self, strategy: CompressionStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: CompressionStrategy) -> None:
        pass

    def compress_file(self, filename: str, data: bytes) -> dict:
        pass  # zwroc {'filename': ..., 'original': ..., 'compressed': ..., 'ratio': ...}


data = b'Hello World! ' * 100
for strategy in [NoCompression(), ZipCompression(), GzipCompression()]:
    compressor = FileCompressor(strategy)
    result = compressor.compress_file('test.txt', data)
    print(result)


# ─── Zadanie 2 ─ Walidator formularza ────────────────────────────────────────
# ValidationStrategy: (value: str) -> bool  (Callable)
# FormValidator.add_rule(name, rule).validate(value) -> list[str] (bledy)
# Reguly: required, min_length(n), max_length(n), matches_pattern(regex)

class FormValidator:
    def __init__(self):
        self._rules: list[tuple[str, Callable]] = []

    def add_rule(self, name: str, rule: Callable[[str], bool]) -> 'FormValidator':
        pass

    def validate(self, value: str) -> list[str]:
        pass  # zwroc liste nazw regul ktore sie nie powiodly


import re

required = lambda v: bool(v.strip())
min_length = lambda n: lambda v: len(v) >= n
max_length = lambda n: lambda v: len(v) <= n
matches_pattern = lambda pattern: lambda v: bool(re.match(pattern, v))

email_validator = (FormValidator()
    .add_rule('required', required)
    .add_rule('min_length_5', min_length(5))
    .add_rule('email_format', matches_pattern(r'^[^@]+@[^@]+\.[^@]+$')))

for email in ['', 'a@b', 'valid@email.com', 'no_at_sign']:
    errors = email_validator.validate(email)
    print(f'{email!r:25}: {errors or "OK"}')


# ─── Zadanie 3 ─ Strategie routingu *(Trudniejsze)* ──────────────────────────
# RoutingStrategy.find_route(origin, destination) -> list[str]
# ShortestPath, FastestPath, EcoPath (najmniej paliwa)
# Navigator(strategy).navigate(origin, destination) -> dict

class RoutingStrategy(ABC):
    @abstractmethod
    def find_route(self, origin: str, destination: str) -> list[str]: ...
    @abstractmethod
    def estimated_time(self, route: list[str]) -> int: ...  # minuty
    @abstractmethod
    def estimated_fuel(self, route: list[str]) -> float: ...  # litry

class ShortestPath(RoutingStrategy):
    def find_route(self, origin: str, destination: str) -> list[str]:
        return [origin, 'via_center', destination]
    def estimated_time(self, route: list[str]) -> int: return len(route) * 5
    def estimated_fuel(self, route: list[str]) -> float: return len(route) * 0.5

class FastestPath(RoutingStrategy):
    def find_route(self, origin: str, destination: str) -> list[str]:
        return [origin, 'via_highway', destination]
    def estimated_time(self, route: list[str]) -> int: return len(route) * 3
    def estimated_fuel(self, route: list[str]) -> float: return len(route) * 0.8

class EcoPath(RoutingStrategy):
    def find_route(self, origin: str, destination: str) -> list[str]:
        return [origin, 'via_eco_road', 'scenic_route', destination]
    def estimated_time(self, route: list[str]) -> int: return len(route) * 8
    def estimated_fuel(self, route: list[str]) -> float: return len(route) * 0.3

class Navigator:
    def __init__(self, strategy: RoutingStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: RoutingStrategy) -> None:
        pass

    def navigate(self, origin: str, destination: str) -> dict:
        # hint: uzyj strategy aby wyliczyc route, czas, paliwo
        pass


nav = Navigator(ShortestPath())
print(nav.navigate('Home', 'Work'))
nav.set_strategy(FastestPath())
print(nav.navigate('Home', 'Work'))
nav.set_strategy(EcoPath())
print(nav.navigate('Home', 'Work'))
