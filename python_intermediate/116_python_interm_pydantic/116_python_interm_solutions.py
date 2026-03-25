"""116 Python intermediate - Pydantic - rozwiązania."""
from pydantic import (
    BaseModel, Field, ValidationError,
    field_validator, model_validator, computed_field, ConfigDict,
)
from typing import Optional, Any, Self
from datetime import date
import json


# ---------------------------------------------------------------------------
# Ćw. 1: Product
# ---------------------------------------------------------------------------
class Product(BaseModel):
    id:       int
    name:     str
    price:    float
    in_stock: bool = True
    tags:     list[str] = []


p1 = Product(id=1, name="Laptop", price=3499.99)
p2 = Product(id=2, name="Mouse", price=49.99, tags=["wireless", "usb"])
print(p1.model_dump())
print(p2.model_dump())

try:
    Product(id="x", name="", price=-10)
except ValidationError as e:
    print(e)


# ---------------------------------------------------------------------------
# Ćw. 2: Author + Book
# ---------------------------------------------------------------------------
class Author(BaseModel):
    name: str
    born: Optional[int] = None


class Book(BaseModel):
    title:  str
    year:   int
    author: Author
    genres: list[str] = []


book = Book(
    title="Clean Code",
    year=2008,
    author={"name": "Robert Martin", "born": 1952},
    genres=["programming", "best practices"],
)
print(book.author.name)
print(book.model_dump())
print(book.model_dump_json(indent=2))


# ---------------------------------------------------------------------------
# Ćw. 3: load_users
# ---------------------------------------------------------------------------
class User(BaseModel):
    id:    int
    name:  str
    email: str


def load_users(json_str: str) -> list[User]:
    records = json.loads(json_str)
    result = []
    for record in records:
        try:
            result.append(User.model_validate(record))
        except ValidationError:
            pass
    return result


sample = json.dumps([
    {"id": 1, "name": "Alice", "email": "a@x.com"},
    {"id": "bad", "name": "Bob", "email": "b@x.com"},
    {"id": 3, "name": "Carol", "email": "c@x.com"},
])
users = load_users(sample)
print(f"Loaded {len(users)} valid users")
for u in users:
    print(u)


# ---------------------------------------------------------------------------
# Ćw. 4: Order
# ---------------------------------------------------------------------------
class Order(BaseModel):
    order_id: int          = Field(gt=0)
    customer: str          = Field(min_length=2, max_length=50)
    items:    list[str]    = Field(min_length=1)
    total:    float        = Field(ge=0)
    status:   str          = "pending"


o = Order(order_id=1, customer="Alice", items=["book", "pen"], total=29.99)
print(o.model_dump())

try:
    Order(order_id=0, customer="A", items=[], total=-5)
except ValidationError as e:
    for err in e.errors():
        print(f"{err['loc']}: {err['msg']}")


# ---------------------------------------------------------------------------
# Ćw. 5: Config z aliasami
# ---------------------------------------------------------------------------
class Config(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    host:    str   = Field(alias="server_host")
    port:    int   = Field(ge=1024, le=65535, alias="server_port")
    debug:   bool  = False
    timeout: float = Field(default=30.0, gt=0, le=300)


cfg = Config.model_validate({"server_host": "localhost", "server_port": 8080})
print(cfg.host, cfg.port)
print(cfg.model_dump(by_alias=True))


# ---------------------------------------------------------------------------
# Ćw. 6: Cart z computed_field
# ---------------------------------------------------------------------------
class CartItem(BaseModel):
    product_id: int
    name:       str
    price:      float = Field(ge=0)
    quantity:   int   = Field(ge=1)


class Cart(BaseModel):
    user_id: int
    items:   list[CartItem] = Field(default_factory=list)

    @computed_field
    @property
    def total(self) -> float:
        return sum(item.price * item.quantity for item in self.items)


cart = Cart(user_id=1, items=[
    {"product_id": 1, "name": "Book", "price": 49.99, "quantity": 2},
    {"product_id": 2, "name": "Pen",  "price":  4.99, "quantity": 5},
])
print(f"Total: {cart.total:.2f}")   # 124.93


# ---------------------------------------------------------------------------
# Ćw. 7: Password validator
# ---------------------------------------------------------------------------
class Password(BaseModel):
    value: str

    @field_validator("value")
    @classmethod
    def strong_password(cls, v: str) -> str:
        if len(v) < 8:
            raise ValueError("Password must be at least 8 characters")
        if not any(c.isdigit() for c in v):
            raise ValueError("Password must contain at least one digit")
        if not any(c.isupper() for c in v):
            raise ValueError("Password must contain at least one uppercase letter")
        return v


try:
    Password(value="short")
except ValidationError as e:
    print(e)

try:
    Password(value="alllowercase1")
except ValidationError as e:
    print(e)

p = Password(value="Secure123")
print(p.value)


# ---------------------------------------------------------------------------
# Ćw. 8: DateRange
# ---------------------------------------------------------------------------
class DateRange(BaseModel):
    start: date
    end:   date

    @model_validator(mode="after")
    def check_order(self) -> Self:
        if self.start >= self.end:
            raise ValueError("start must be before end")
        return self


dr = DateRange(start="2024-01-01", end="2024-12-31")
print(dr.start, dr.end)

try:
    DateRange(start="2024-12-31", end="2024-01-01")
except ValidationError as e:
    print(e)


# ---------------------------------------------------------------------------
# Ćw. 9: Invoice z computed_field
# ---------------------------------------------------------------------------
class InvoiceItem(BaseModel):
    name:  str
    price: float = Field(ge=0)
    qty:   int   = Field(ge=1)


class Invoice(BaseModel):
    items:    list[InvoiceItem]
    discount: float = Field(default=0.0, ge=0.0, le=1.0)

    @computed_field
    @property
    def subtotal(self) -> float:
        return sum(item.price * item.qty for item in self.items)

    @computed_field
    @property
    def total_after_discount(self) -> float:
        return self.subtotal * (1 - self.discount)


inv = Invoice(
    items=[
        {"name": "Widget", "price": 100.0, "qty": 3},
        {"name": "Gadget", "price":  50.0, "qty": 2},
    ],
    discount=0.1,
)
print(f"Subtotal: {inv.subtotal:.2f}")                   # 400.00
print(f"After discount: {inv.total_after_discount:.2f}") # 360.00


# ---------------------------------------------------------------------------
# Ćw. 10: Tag z ConfigDict
# ---------------------------------------------------------------------------
class Tag(BaseModel):
    model_config = ConfigDict(
        str_strip_whitespace=True,
        str_to_lower=True,
        frozen=True,
    )
    name: str


t = Tag(name="  Python  ")
print(repr(t.name))   # 'python'

try:
    t.name = "java"
except Exception as e:
    print(type(e).__name__)


# ---------------------------------------------------------------------------
# Ćw. 11: ApiResponse z extra='forbid'
# ---------------------------------------------------------------------------
class ApiResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")
    status:  int
    data:    dict
    message: str = ""


r = ApiResponse(status=200, data={"users": []})
print(r)

try:
    ApiResponse(status=200, data={}, meta={"page": 1})
except ValidationError as e:
    print(e)


# ---------------------------------------------------------------------------
# Ćw. 12: DatabaseConfig z computed url
# ---------------------------------------------------------------------------
class DatabaseConfig(BaseModel):
    host:     str
    port:     int = 5432
    name:     str
    user:     str
    password: str

    @computed_field
    @property
    def url(self) -> str:
        return (
            f"postgresql://{self.user}:{self.password}"
            f"@{self.host}:{self.port}/{self.name}"
        )


db = DatabaseConfig(
    host="localhost", name="mydb",
    user="admin", password="secret",
)
print(db.url)   # postgresql://admin:secret@localhost:5432/mydb
