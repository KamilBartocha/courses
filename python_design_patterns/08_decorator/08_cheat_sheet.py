# 08_cheat_sheet.py - Decorator (Dekorator)

import functools
import time
from abc import ABC, abstractmethod


# ── Dekorator obiektowy (klasyczny GoF) ──────────────────────────────────────
class Beverage(ABC):
    @abstractmethod
    def cost(self) -> float: ...
    @abstractmethod
    def description(self) -> str: ...

class Espresso(Beverage):
    def cost(self) -> float: return 5.0
    def description(self) -> str: return 'Espresso'

class BeverageDecorator(Beverage):
    def __init__(self, beverage: Beverage):
        self._beverage = beverage
    def cost(self) -> float: return self._beverage.cost()
    def description(self) -> str: return self._beverage.description()

class MilkDecorator(BeverageDecorator):
    def cost(self) -> float: return self._beverage.cost() + 1.5
    def description(self) -> str: return self._beverage.description() + ' + milk'

class CaramelDecorator(BeverageDecorator):
    def cost(self) -> float: return self._beverage.cost() + 2.0
    def description(self) -> str: return self._beverage.description() + ' + caramel'

drink = CaramelDecorator(MilkDecorator(Espresso()))
print(drink.description(), '->', drink.cost())


# ── Dekorator Pythona (@) ─────────────────────────────────────────────────────
def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f'{func.__name__}: {elapsed:.4f}s')
        return result
    return wrapper

def logger(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f'Calling {func.__name__}({args}, {kwargs})')
        result = func(*args, **kwargs)
        print(f'{func.__name__} returned {result}')
        return result
    return wrapper

@timer
@logger
def compute(n: int) -> int:
    return sum(range(n))

compute(1_000_000)


# ── Dekorator parametryzowany ─────────────────────────────────────────────────
def retry(max_attempts: int = 3, delay: float = 0.1):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exc = None
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exc = e
                    print(f'Attempt {attempt} failed: {e}')
                    time.sleep(delay)
            raise last_exc
        return wrapper
    return decorator

@retry(max_attempts=3, delay=0.01)
def unstable_call(n: int) -> str:
    import random
    if random.random() < 0.7:
        raise ConnectionError('timeout')
    return f'ok({n})'

try:
    print(unstable_call(1))
except ConnectionError:
    print('All attempts failed')


# ── functools.lru_cache ───────────────────────────────────────────────────────
@functools.lru_cache(maxsize=128)
def fibonacci(n: int) -> int:
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(40))
print(fibonacci.cache_info())  # hits, misses, maxsize, currsize


# ── functools.singledispatch ──────────────────────────────────────────────────
@functools.singledispatch
def format_value(value) -> str:
    return str(value)

@format_value.register(int)
def _(value: int) -> str:
    return f'{value:,}'

@format_value.register(float)
def _(value: float) -> str:
    return f'{value:.2f}'

@format_value.register(list)
def _(value: list) -> str:
    return '[' + ', '.join(format_value(v) for v in value) + ']'

print(format_value(1234567))     # 1,234,567
print(format_value(3.14159))     # 3.14
print(format_value([1, 2.5, 3])) # [1, 2.50, 3]
