"""15 Python intermediate - Adnotacje typów (typing) - rozwiązania."""
from typing import Optional, Union, Callable, Any, TypeVar, Generic, Protocol
from typing import runtime_checkable, Literal
import math


# ---------------------------------------------------------------------------
# Ćw. 1: Adnotacje dla calculate_bmi, get_initials, flatten_once
# ---------------------------------------------------------------------------
def calculate_bmi(weight_kg: float, height_m: float) -> float:
    return weight_kg / height_m ** 2


def get_initials(full_name: str) -> str:
    return ".".join(part[0].upper() for part in full_name.split()) + "."


def flatten_once(nested: list[list]) -> list:
    return [item for sublist in nested for item in sublist]


print(f"{calculate_bmi(70, 1.75):.1f}")          # 22.9
print(get_initials("John Doe"))                    # J.D.
print(flatten_once([[1, 2], [3], [4, 5]]))         # [1, 2, 3, 4, 5]


# ---------------------------------------------------------------------------
# Ćw. 2: Point z distance_to i midpoint
# ---------------------------------------------------------------------------
class Point:
    x: float
    y: float

    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def distance_to(self, other: "Point") -> float:
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def midpoint(self, other: "Point") -> "Point":
        return Point((self.x + other.x) / 2, (self.y + other.y) / 2)

    def __repr__(self) -> str:
        return f"Point({self.x}, {self.y})"


p1 = Point(0, 0)
p2 = Point(3, 4)
print(p1.distance_to(p2))   # 5.0
print(p1.midpoint(p2))      # Point(1.5, 2.0)


# ---------------------------------------------------------------------------
# Ćw. 3: group_by
# ---------------------------------------------------------------------------
def group_by(items: list, key_func) -> dict:
    result: dict = {}
    for item in items:
        key = key_func(item)
        if key not in result:
            result[key] = []
        result[key].append(item)
    return result


words = ["apple", "ant", "banana", "bear", "cherry", "cat"]
grouped = group_by(words, lambda w: w[0])
print(grouped)


# ---------------------------------------------------------------------------
# Ćw. 4: safe_parse_int, parse_list
# ---------------------------------------------------------------------------
def safe_parse_int(text: str) -> Optional[int]:
    try:
        return int(text)
    except ValueError:
        return None


def parse_list(texts: list[str]) -> list[int]:
    return [v for t in texts if (v := safe_parse_int(t)) is not None]


print(safe_parse_int("42"))             # 42
print(safe_parse_int("abc"))            # None
print(parse_list(["1", "2", "x", "4"])) # [1, 2, 4]


# ---------------------------------------------------------------------------
# Ćw. 5: transform z TypeVar
# ---------------------------------------------------------------------------
T = TypeVar("T")
R = TypeVar("R")


def transform(data: list[T], func: Callable[[T], R]) -> list[R]:
    return [func(item) for item in data]


print(transform([1, 2, 3, 4], lambda x: x ** 2))
print(transform(["hello", "world"], str.upper))


# ---------------------------------------------------------------------------
# Ćw. 6: align_text i make_border z Literal
# ---------------------------------------------------------------------------
Alignment   = Literal["left", "center", "right"]
BorderStyle = Literal["single", "double"]


def align_text(text: str, alignment: Alignment, width: int = 40) -> str:
    if alignment == "left":
        return text.ljust(width)
    if alignment == "center":
        return text.center(width)
    return text.rjust(width)


def make_border(style: BorderStyle, width: int = 40) -> str:
    char = "─" if style == "single" else "═"
    return char * width


print(align_text("Hello", "left"))
print(align_text("Hello", "center"))
print(align_text("Hello", "right"))
print(make_border("single"))
print(make_border("double"))


# ---------------------------------------------------------------------------
# Ćw. 7: deep_get
# ---------------------------------------------------------------------------
def deep_get(d: dict, *keys: str) -> Optional[Any]:
    current = d
    for key in keys:
        if not isinstance(current, dict):
            return None
        current = current.get(key)
    return current


data = {"user": {"name": "Alice", "address": {"city": "Warsaw"}}}
print(deep_get(data, "user", "name"))              # Alice
print(deep_get(data, "user", "address", "city"))   # Warsaw
print(deep_get(data, "user", "phone"))             # None
print(deep_get(data, "missing", "key"))            # None


# ---------------------------------------------------------------------------
# Ćw. 8: last, zip_with
# ---------------------------------------------------------------------------
def last(items: list[T]) -> T:
    return items[-1]


def zip_with(
    a: list[T],
    b: list[T],
    func: Callable[[T, T], R],
) -> list[R]:
    return [func(x, y) for x, y in zip(a, b)]


print(last([1, 2, 3]))          # 3
print(last(["x", "y", "z"]))   # 'z'
print(zip_with([1, 2, 3], [4, 5, 6], lambda a, b: a + b))  # [5, 7, 9]


# ---------------------------------------------------------------------------
# Ćw. 9: Pair[T, U]
# ---------------------------------------------------------------------------
U = TypeVar("U")


class Pair(Generic[T, U]):
    def __init__(self, first: T, second: U) -> None:
        self.first = first
        self.second = second

    def swap(self) -> "Pair[U, T]":
        return Pair(self.second, self.first)

    def map_first(self, func: Callable[[T], R]) -> "Pair[R, U]":
        return Pair(func(self.first), self.second)

    def __repr__(self) -> str:
        return f"Pair({self.first!r}, {self.second!r})"


p = Pair(1, "hello")
print(p)                               # Pair(1, 'hello')
print(p.swap())                        # Pair('hello', 1)
print(p.map_first(lambda x: x * 10))  # Pair(10, 'hello')


# ---------------------------------------------------------------------------
# Ćw. 10: binary_search z Protocol Comparable
# ---------------------------------------------------------------------------
@runtime_checkable
class Comparable(Protocol):
    def __lt__(self, other) -> bool: ...
    def __eq__(self, other) -> bool: ...


TC = TypeVar("TC", bound=Comparable)


def binary_search(items: list[TC], target: TC) -> int:
    lo, hi = 0, len(items) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if items[mid] == target:
            return mid
        elif items[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


print(binary_search([1, 3, 5, 7, 9, 11], 7))                          # 3
print(binary_search([1, 3, 5, 7, 9, 11], 4))                          # -1
print(binary_search(["apple", "banana", "cherry", "date"], "cherry"))  # 2
