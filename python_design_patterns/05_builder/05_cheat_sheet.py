# 05_cheat_sheet.py - Builder (Budowniczy)

from dataclasses import dataclass, field
from typing import Optional


# ── Produkt ───────────────────────────────────────────────────────────────────
@dataclass
class Pizza:
    size: str
    crust: str
    sauce: str
    toppings: list[str]
    extra_cheese: bool = False

    def __repr__(self) -> str:
        tops = ", ".join(self.toppings) or "none"
        return (f"Pizza({self.size}, {self.crust} crust, "
                f"{self.sauce} sauce, toppings: [{tops}], "
                f"extra cheese: {self.extra_cheese})")


# ── Builder z fluent interface ────────────────────────────────────────────────
class PizzaBuilder:
    def __init__(self) -> None:
        self._size = "medium"
        self._crust = "thin"
        self._sauce = "tomato"
        self._toppings: list[str] = []
        self._extra_cheese = False

    def size(self, size: str) -> "PizzaBuilder":
        self._size = size
        return self

    def crust(self, crust: str) -> "PizzaBuilder":
        self._crust = crust
        return self

    def sauce(self, sauce: str) -> "PizzaBuilder":
        self._sauce = sauce
        return self

    def add_topping(self, topping: str) -> "PizzaBuilder":
        self._toppings.append(topping)
        return self

    def extra_cheese(self) -> "PizzaBuilder":
        self._extra_cheese = True
        return self

    def build(self) -> Pizza:
        return Pizza(
            size=self._size,
            crust=self._crust,
            sauce=self._sauce,
            toppings=self._toppings[:],
            extra_cheese=self._extra_cheese,
        )

pizza = (PizzaBuilder()
         .size("large")
         .crust("thick")
         .sauce("pesto")
         .add_topping("mushrooms")
         .add_topping("olives")
         .extra_cheese()
         .build())
print(pizza)


# ── Builder z walidacja ───────────────────────────────────────────────────────
class QueryBuilder:
    def __init__(self) -> None:
        self._table: Optional[str] = None
        self._conditions: list[str] = []
        self._limit: Optional[int] = None
        self._columns: list[str] = ["*"]

    def from_table(self, table: str) -> "QueryBuilder":
        self._table = table
        return self

    def select(self, *columns: str) -> "QueryBuilder":
        self._columns = list(columns)
        return self

    def where(self, condition: str) -> "QueryBuilder":
        self._conditions.append(condition)
        return self

    def limit(self, n: int) -> "QueryBuilder":
        self._limit = n
        return self

    def build(self) -> str:
        if not self._table:
            raise ValueError("Table name is required")
        cols = ", ".join(self._columns)
        sql = f"SELECT {cols} FROM {self._table}"
        if self._conditions:
            sql += " WHERE " + " AND ".join(self._conditions)
        if self._limit:
            sql += f" LIMIT {self._limit}"
        return sql

query = (QueryBuilder()
         .from_table("users")
         .select("id", "name", "email")
         .where("age > 18")
         .where("active = true")
         .limit(10)
         .build())
print(query)
# SELECT id, name, email FROM users WHERE age > 18 AND active = true LIMIT 10


# ── Dyrektor ──────────────────────────────────────────────────────────────────
class PizzaDirector:
    @staticmethod
    def make_margherita(builder: PizzaBuilder) -> Pizza:
        return (builder
                .size("medium")
                .crust("thin")
                .sauce("tomato")
                .add_topping("mozzarella")
                .build())

    @staticmethod
    def make_veggie(builder: PizzaBuilder) -> Pizza:
        return (builder
                .size("large")
                .crust("thick")
                .sauce("pesto")
                .add_topping("peppers")
                .add_topping("spinach")
                .add_topping("onion")
                .build())

margherita = PizzaDirector.make_margherita(PizzaBuilder())
veggie = PizzaDirector.make_veggie(PizzaBuilder())
print(margherita)
print(veggie)
