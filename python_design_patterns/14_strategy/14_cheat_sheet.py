# 14_cheat_sheet.py - Strategy (Strategia)

from abc import ABC, abstractmethod
from typing import Callable


# ── Klasyczna implementacja ───────────────────────────────────────────────────
class SortStrategy(ABC):
    @abstractmethod
    def sort(self, data: list) -> list: ...

class BubbleSort(SortStrategy):
    def sort(self, data: list) -> list:
        arr = data[:]
        n = len(arr)
        for i in range(n):
            for j in range(n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr

class QuickSort(SortStrategy):
    def sort(self, data: list) -> list:
        if len(data) <= 1: return data[:]
        pivot = data[len(data) // 2]
        left = [x for x in data if x < pivot]
        mid = [x for x in data if x == pivot]
        right = [x for x in data if x > pivot]
        return self.sort(left) + mid + self.sort(right)

class Sorter:
    def __init__(self, strategy: SortStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: SortStrategy) -> None:
        self._strategy = strategy

    def sort(self, data: list) -> list:
        return self._strategy.sort(data)

data = [64, 34, 25, 12, 22, 11, 90]
sorter = Sorter(BubbleSort())
print('Bubble:', sorter.sort(data))
sorter.set_strategy(QuickSort())
print('Quick:', sorter.sort(data))


# ── Strategia jako funkcja (pierwszorzedny obywatel) ─────────────────────────
class Validator:
    def __init__(self) -> None:
        self._strategies: list[Callable[[str], bool]] = []

    def add_rule(self, rule: Callable[[str], bool]) -> 'Validator':
        self._strategies.append(rule)
        return self

    def validate(self, value: str) -> list[str]:
        return [rule.__name__ for rule in self._strategies if not rule(value)]

def not_empty(s: str) -> bool: return bool(s.strip())
def min_length_8(s: str) -> bool: return len(s) >= 8
def has_digit(s: str) -> bool: return any(c.isdigit() for c in s)
def has_upper(s: str) -> bool: return any(c.isupper() for c in s)

password_validator = (Validator()
    .add_rule(not_empty)
    .add_rule(min_length_8)
    .add_rule(has_digit)
    .add_rule(has_upper))

for pwd in ['', 'short', 'longenough', 'LongWithUpper1']:
    errors = password_validator.validate(pwd)
    status = 'OK' if not errors else f'Failed: {errors}'
    print(f'{pwd!r:20}: {status}')


# ── Rejestr strategii ────────────────────────────────────────────────────────
class PaymentContext:
    _strategies: dict[str, Callable[[float], bool]] = {}

    @classmethod
    def register(cls, name: str) -> Callable:
        def decorator(func: Callable) -> Callable:
            cls._strategies[name] = func
            return func
        return decorator

    def __init__(self, method: str) -> None:
        if method not in self._strategies:
            raise ValueError(f'Unknown payment method: {method}')
        self._strategy = self._strategies[method]

    def pay(self, amount: float) -> bool:
        return self._strategy(amount)

@PaymentContext.register('card')
def pay_by_card(amount: float) -> bool:
    print(f'Card: {amount} PLN')
    return True

@PaymentContext.register('blik')
def pay_by_blik(amount: float) -> bool:
    print(f'BLIK: {amount} PLN')
    return True

PaymentContext('card').pay(99.99)
PaymentContext('blik').pay(49.50)
