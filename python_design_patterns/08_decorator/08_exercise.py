# 08_exercise.py - Decorator (Dekorator)

import functools
import time
from abc import ABC, abstractmethod

# ─── Zadanie 1 ─ Dekorator obiektowy GoF ──────────────────────────────────────
# Napisz hierarchie TextProcessor z metoda process(text: str) -> str.
# Konkretne: PlainText (zwraca bez zmian).
# Dekoratory: UpperCaseDecorator, TrimDecorator, PrefixDecorator(prefix).

class TextProcessor(ABC):
    @abstractmethod
    def process(self, text: str) -> str: ...

class PlainText(TextProcessor):
    def process(self, text: str) -> str: return text

class TextDecorator(TextProcessor):
    def __init__(self, processor: TextProcessor):
        self._processor = processor
    def process(self, text: str) -> str:
        return self._processor.process(text)

class UpperCaseDecorator(TextDecorator):
    def process(self, text: str) -> str: pass

class TrimDecorator(TextDecorator):
    def process(self, text: str) -> str: pass

class PrefixDecorator(TextDecorator):
    def __init__(self, processor: TextProcessor, prefix: str):
        super().__init__(processor)
        self.prefix = prefix
    def process(self, text: str) -> str: pass


pipeline = PrefixDecorator(UpperCaseDecorator(TrimDecorator(PlainText())), '>> ')
print(pipeline.process('  hello world  '))  # >> HELLO WORLD


# ─── Zadanie 2 ─ Dekorator Pythona (@) ───────────────────────────────────────
# Napisz dekorator @log_calls ktory drukuje:
# "Calling func_name(args)" przed wywolaniem i
# "func_name returned result" po.
# Uzyj @functools.wraps.

def log_calls(func):
    pass

@log_calls
def add(a: int, b: int) -> int:
    return a + b

@log_calls
def greet(name: str) -> str:
    return f'Hello, {name}!'

add(3, 4)
greet('Alice')
print(add.__name__)  # add (nie wrapper - dzieki functools.wraps)


# ─── Zadanie 3 ─ Dekorator @timer ────────────────────────────────────────────
# Napisz dekorator @timer mierzacy czas wykonania funkcji.
# Drukuj: "func_name: X.XXXXs"

def timer(func):
    pass

@timer
def slow_sum(n: int) -> int:
    return sum(range(n))

result = slow_sum(10_000_000)
print(f'Result: {result}')


# ─── Zadanie 4 ─ Dekorator parametryzowany @validate ──────────────────────────
# Napisz @validate(min_val, max_val) - dekorator dla funkcji
# przyjmujacej jeden argument numeryczny.
# Rzuca ValueError jesli argument jest poza zakresem.

def validate(min_val, max_val):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(value, *args, **kwargs):
            pass
        return wrapper
    return decorator

@validate(0, 100)
def set_volume(level: int) -> str:
    return f'Volume: {level}%'

@validate(1, 31)
def set_day(day: int) -> str:
    return f'Day: {day}'

print(set_volume(50))    # Volume: 50%
print(set_day(15))       # Day: 15
try:
    set_volume(150)      # ValueError: 150 not in [0, 100]
except ValueError as e:
    print(e)


# ─── Zadanie 5 ─ Dekorator @memoize *(Trudniejsze)* ──────────────────────────
# Napisz dekorator @memoize() z parametrem max_size.
# Cache FIFO: jesli przekroczy max_size, usuwa najstarszy wpis.
# Przetestuj na fibonacci(35) - porownaj czas z cache i bez.
# # hint: uzyj collections.OrderedDict

import collections

def memoize(max_size: int = 128):
    def decorator(func):
        cache = collections.OrderedDict()
        @functools.wraps(func)
        def wrapper(*args):
            if args in cache:
                cache.move_to_end(args)
                return cache[args]
            result = func(*args)
            cache[args] = result
            if len(cache) > max_size:
                cache.popitem(last=False)  # usuń najstarszy (FIFO)
            return result
        wrapper.cache = cache
        return wrapper
    return decorator

@memoize(max_size=50)
def fib(n: int) -> int:
    if n < 2: return n
    return fib(n - 1) + fib(n - 2)

start = time.perf_counter()
result = fib(35)
elapsed = time.perf_counter() - start
print(f'fib(35) = {result}')
print(f'Time: {elapsed:.6f}s')
print(f'Cache size: {len(fib.cache)}')
