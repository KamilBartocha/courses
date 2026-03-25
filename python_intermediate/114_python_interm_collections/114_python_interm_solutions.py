"""114 Python intermediate - collections i enum - rozwiązania."""
from collections import Counter, defaultdict, deque, namedtuple
from enum import Enum, IntEnum, Flag, auto
import re


# ---------------------------------------------------------------------------
# Ćw. 1: Counter - analiza tekstów
# ---------------------------------------------------------------------------
text1 = "the cat sat on the mat the cat sat"
text2 = "the dog sat on the log the cat ran"

c1 = Counter(text1.split())
c2 = Counter(text2.split())

top5         = c1.most_common(5)
common       = c1 & c2
unique_to_1  = c1 - c2

print("Top 5:", top5)
print("Common:", dict(common))
print("Unique to text1:", dict(unique_to_1))


# ---------------------------------------------------------------------------
# Ćw. 2: defaultdict - transakcje
# ---------------------------------------------------------------------------
transactions = [
    ("Alice", 100), ("Bob", 50), ("Alice", 200),
    ("Carol", 75),  ("Bob", 30), ("Alice", 50),
]
by_user = defaultdict(list)
for name, amount in transactions:
    by_user[name].append(amount)

totals = {name: sum(amounts) for name, amounts in by_user.items()}
print(totals)   # {'Alice': 350, 'Bob': 80, 'Carol': 75}


# ---------------------------------------------------------------------------
# Ćw. 3: word_frequency + hapax
# ---------------------------------------------------------------------------
def word_frequency(text: str) -> Counter:
    cleaned = re.sub(r"[^\w\s]", "", text.lower())
    return Counter(cleaned.split())


sample = ("To be or not to be, that is the question. "
          "Whether tis nobler in the mind to suffer.")
freq = word_frequency(sample)
print(freq.most_common(5))
hapax = [w for w, c in freq.items() if c == 1]
print("Hapax:", sorted(hapax))


# ---------------------------------------------------------------------------
# Ćw. 4: Queue z deque
# ---------------------------------------------------------------------------
class Queue:
    def __init__(self):
        self._data = deque()

    def enqueue(self, item) -> None:
        self._data.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self._data.popleft()

    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self._data[0]

    def is_empty(self) -> bool:
        return len(self._data) == 0

    def __len__(self) -> int:
        return len(self._data)


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(len(q), q.peek(), q.dequeue(), len(q))   # 3 1 1 2


# ---------------------------------------------------------------------------
# Ćw. 5: namedtuple - Employee
# ---------------------------------------------------------------------------
Employee = namedtuple("Employee", ["name", "department", "salary"])

employees = [
    Employee("Alice", "Engineering", 9000),
    Employee("Bob",   "Marketing",   7000),
    Employee("Carol", "Engineering", 8500),
    Employee("Dave",  "Marketing",   6500),
    Employee("Eve",   "Engineering", 9500),
]

sorted_emp = sorted(employees, key=lambda e: (e.department, -e.salary))
print(sorted_emp)

dept_groups = defaultdict(list)
for emp in employees:
    dept_groups[emp.department].append(emp.salary)
avg_salary = {dept: sum(s)/len(s) for dept, s in dept_groups.items()}
print(avg_salary)


# ---------------------------------------------------------------------------
# Ćw. 6: LRUCache
# ---------------------------------------------------------------------------
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache: dict = {}
        self.order: deque = deque()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.order.remove(key)
        self.order.append(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.order.remove(key)
        elif len(self.cache) >= self.capacity:
            oldest = self.order.popleft()
            del self.cache[oldest]
        self.cache[key] = value
        self.order.append(key)


cache = LRUCache(3)
cache.put(1, 10)
cache.put(2, 20)
cache.put(3, 30)
print(cache.get(1))    # 10
cache.put(4, 40)
print(cache.get(2))    # -1
print(cache.get(3))    # 30


# ---------------------------------------------------------------------------
# Ćw. 7: Direction z opposite()
# ---------------------------------------------------------------------------
class Direction(Enum):
    NORTH = "N"
    SOUTH = "S"
    EAST  = "E"
    WEST  = "W"

    def opposite(self) -> "Direction":
        opposites = {
            Direction.NORTH: Direction.SOUTH,
            Direction.SOUTH: Direction.NORTH,
            Direction.EAST:  Direction.WEST,
            Direction.WEST:  Direction.EAST,
        }
        return opposites[self]


for d in Direction:
    print(f"{d.name} -> {d.opposite().name}")


# ---------------------------------------------------------------------------
# Ćw. 8: Priority z filter_tasks
# ---------------------------------------------------------------------------
class Priority(IntEnum):
    LOW      = 1
    MEDIUM   = 2
    HIGH     = 3
    CRITICAL = 4


def filter_tasks(tasks: list, min_priority: Priority) -> list:
    return [(name, p) for name, p in tasks if p >= min_priority]


tasks = [
    ("Write tests",  Priority.HIGH),
    ("Update docs",  Priority.LOW),
    ("Fix prod bug", Priority.CRITICAL),
    ("Code review",  Priority.MEDIUM),
]
print(filter_tasks(tasks, Priority.HIGH))


# ---------------------------------------------------------------------------
# Ćw. 9: Planet Enum
# ---------------------------------------------------------------------------
G = 6.67430e-11


class Planet(Enum):
    MERCURY = (3.303e+23, 2.4397e6)
    VENUS   = (4.869e+24, 6.0518e6)
    EARTH   = (5.976e+24, 6.37814e6)
    MARS    = (6.421e+23, 3.3972e6)

    def __init__(self, mass: float, radius: float):
        self.mass   = mass
        self.radius = radius

    @property
    def surface_gravity(self) -> float:
        return G * self.mass / self.radius ** 2

    def weight(self, mass_on_earth: float) -> float:
        return mass_on_earth * self.surface_gravity


for planet in Planet:
    print(f"{planet.name}: {planet.weight(75):.2f} N")


# ---------------------------------------------------------------------------
# Ćw. 10: Weekday z is_weekend
# ---------------------------------------------------------------------------
class Weekday(Enum):
    MONDAY    = auto()
    TUESDAY   = auto()
    WEDNESDAY = auto()
    THURSDAY  = auto()
    FRIDAY    = auto()
    SATURDAY  = auto()
    SUNDAY    = auto()

    def is_weekend(self) -> bool:
        return self in (Weekday.SATURDAY, Weekday.SUNDAY)


for day in Weekday:
    weekend = "(weekend)" if day.is_weekend() else ""
    print(f"{day.name} {weekend}")


# ---------------------------------------------------------------------------
# Ćw. 11: FileMode z open_mode
# ---------------------------------------------------------------------------
class FileMode(Flag):
    READ   = auto()
    WRITE  = auto()
    APPEND = auto()
    BINARY = auto()


def open_mode(flags: FileMode) -> str:
    if FileMode.APPEND in flags:
        mode = "a"
    elif FileMode.WRITE in flags:
        mode = "w"
    else:
        mode = "r"
    if FileMode.BINARY in flags:
        mode += "b"
    return mode


print(open_mode(FileMode.READ))                     # 'r'
print(open_mode(FileMode.READ | FileMode.BINARY))   # 'rb'
print(open_mode(FileMode.WRITE))                    # 'w'
print(open_mode(FileMode.APPEND | FileMode.BINARY)) # 'ab'


# ---------------------------------------------------------------------------
# Ćw. 12: Status z can_transition_to
# ---------------------------------------------------------------------------
class Status(Enum):
    PENDING    = auto()
    PROCESSING = auto()
    SHIPPED    = auto()
    DELIVERED  = auto()
    CANCELLED  = auto()

    _TRANSITIONS = None   # inicjalizacja poza ciałem klasy

    def can_transition_to(self, next_status: "Status") -> bool:
        allowed = {
            Status.PENDING:    {Status.PROCESSING, Status.CANCELLED},
            Status.PROCESSING: {Status.SHIPPED,    Status.CANCELLED},
            Status.SHIPPED:    {Status.DELIVERED,  Status.CANCELLED},
            Status.DELIVERED:  set(),
            Status.CANCELLED:  set(),
        }
        return next_status in allowed.get(self, set())


s = Status.PENDING
print(s.can_transition_to(Status.PROCESSING))   # True
print(s.can_transition_to(Status.DELIVERED))    # False
print(s.can_transition_to(Status.CANCELLED))    # True
