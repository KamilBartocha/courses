# 11_exercise.py - Composite (Kompozyt)

from abc import ABC, abstractmethod

# ─── Zadanie 1 ─ Struktura organizacyjna ──────────────────────────────────────
# Napisz hierarchie dla struktury firmy:
# Employee.get_salary() -> float, display(indent)
# Department.add(e), get_salary() (suma), display(indent)

class OrgComponent(ABC):
    @abstractmethod
    def get_salary(self) -> float: ...
    @abstractmethod
    def display(self, indent: int = 0) -> None: ...

class Employee(OrgComponent):
    def __init__(self, name: str, salary: float):
        self.name = name
        self._salary = salary
    def get_salary(self) -> float: pass
    def display(self, indent: int = 0) -> None: pass

class Department(OrgComponent):
    def __init__(self, name: str):
        self.name = name
        self._members: list[OrgComponent] = []
    def add(self, member: OrgComponent) -> None: pass
    def get_salary(self) -> float: pass
    def display(self, indent: int = 0) -> None: pass


company = Department('TechCorp')
dev = Department('Development')
dev.add(Employee('Alice', 8000))
dev.add(Employee('Bob', 7500))
sales = Department('Sales')
sales.add(Employee('Charlie', 6000))
company.add(dev)
company.add(sales)
company.add(Employee('Diana', 12000))  # CEO
company.display()
print(f'Total salaries: {company.get_salary()} PLN')


# ─── Zadanie 2 ─ Wyrazenia matematyczne ───────────────────────────────────────
# Expression.evaluate() -> float, __str__() -> str
# Number(value), Add(left, right), Multiply(left, right)

class Expression(ABC):
    @abstractmethod
    def evaluate(self) -> float: ...
    @abstractmethod
    def __str__(self) -> str: ...

class Number(Expression):
    def __init__(self, value: float): self.value = value
    def evaluate(self) -> float: pass
    def __str__(self) -> str: pass

class Add(Expression):
    def __init__(self, left: Expression, right: Expression):
        self.left = left; self.right = right
    def evaluate(self) -> float: pass
    def __str__(self) -> str: pass

class Multiply(Expression):
    def __init__(self, left: Expression, right: Expression):
        self.left = left; self.right = right
    def evaluate(self) -> float: pass
    def __str__(self) -> str: pass


# (3 + 4) * 2
expr = Multiply(Add(Number(3), Number(4)), Number(2))
print(f'{expr} = {expr.evaluate()}')  # (3 + 4) * 2 = 14.0


# ─── Zadanie 3 ─ Zadania projektowe *(Trudniejsze)* ──────────────────────────
# Task.complete() -> None, is_done() -> bool, __str__() -> str
# SimpleTask, CompositeTask.add(task), is_done() -> True tylko gdy wszystkie done

class Task(ABC):
    @abstractmethod
    def complete(self) -> None: ...
    @abstractmethod
    def is_done(self) -> bool: ...
    @abstractmethod
    def __str__(self) -> str: ...

class SimpleTask(Task):
    def __init__(self, name: str): self.name = name; self._done = False
    def complete(self) -> None: pass
    def is_done(self) -> bool: pass
    def __str__(self) -> str: pass

class CompositeTask(Task):
    def __init__(self, name: str):
        self.name = name
        self._tasks: list[Task] = []
    def add(self, task: Task) -> None: pass
    def complete(self) -> None: pass  # oznacza wszystkie jako done
    def is_done(self) -> bool: pass
    def __str__(self) -> str: pass


feature = CompositeTask('Feature: Login')
feature.add(SimpleTask('Design UI'))
feature.add(SimpleTask('Backend API'))
review = CompositeTask('Code Review')
review.add(SimpleTask('Review PR'))
review.add(SimpleTask('Fix comments'))
feature.add(review)

print(feature)
print(f'Done: {feature.is_done()}')
# hint: complete first subtask
feature._tasks[0].complete()
feature._tasks[1].complete()
feature._tasks[2].complete()
print(f'Done after all: {feature.is_done()}')
