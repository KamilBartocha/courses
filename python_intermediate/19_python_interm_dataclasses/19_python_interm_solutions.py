"""
Module 19 - dataclasses solutions
"""
from dataclasses import dataclass, field, asdict, astuple, replace, InitVar
from typing import ClassVar, NamedTuple, TypedDict
import math
import sys


# Ćw. 1 - Product
@dataclass
class Product:
    name:  str
    price: float
    stock: int       = 0
    tags:  list[str] = field(default_factory=list)

    def is_available(self) -> bool:
        return self.stock > 0


# Ćw. 2 - Vector2D
@dataclass
class Vector2D:
    x: float
    y: float
    length_cached: float = field(init=False, compare=False)

    def __post_init__(self):
        self.length_cached = math.sqrt(self.x**2 + self.y**2)

    def __add__(self, other: 'Vector2D') -> 'Vector2D':
        return Vector2D(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar: float) -> 'Vector2D':
        return Vector2D(self.x * scalar, self.y * scalar)

    def length(self) -> float:
        return self.length_cached


# Ćw. 3 - Student sortowany po grade
@dataclass(order=True)
class Student:
    grade:      float
    name:       str = field(compare=False)
    student_id: int = field(compare=False)


# Ćw. 4 - Rectangle z post_init
@dataclass
class Rectangle:
    width:     float
    height:    float
    area:      float = field(init=False, repr=False)
    perimeter: float = field(init=False, repr=False)

    def __post_init__(self):
        if self.width <= 0 or self.height <= 0:
            raise ValueError('Wymiary muszą być dodatnie')
        self.area = self.width * self.height
        self.perimeter = 2 * (self.width + self.height)


# Ćw. 5 - User z ClassVar
@dataclass
class User:
    first_name: str
    last_name:  str
    email:      str
    count:      ClassVar[int] = 0
    full_name:  str = field(init=False)

    def __post_init__(self):
        User.count += 1
        self.full_name = f'{self.first_name} {self.last_name}'


# Ćw. 6 - Temperature z InitVar
@dataclass
class Temperature:
    value:   float
    unit:    InitVar[str] = 'C'
    celsius: float = field(init=False)

    def __post_init__(self, unit: str):
        if unit == 'C':
            self.celsius = self.value
        elif unit == 'F':
            self.celsius = (self.value - 32) * 5 / 9
        elif unit == 'K':
            self.celsius = self.value - 273.15
        else:
            raise ValueError(f'Nieznana jednostka: {unit}')

    def to_fahrenheit(self) -> float:
        return self.celsius * 9 / 5 + 32

    def to_kelvin(self) -> float:
        return self.celsius + 273.15


# Ćw. 7 - Color frozen
@dataclass(frozen=True)
class Color:
    r: int
    g: int
    b: int

    def __post_init__(self):
        for name, val in [('r', self.r), ('g', self.g), ('b', self.b)]:
            if not 0 <= val <= 255:
                raise ValueError(f'{name}={val} poza zakresem 0-255')


# Ćw. 8 - Shape hierarchy
@dataclass(frozen=True)
class Shape:
    color: str = 'black'

    def area(self) -> float:
        raise NotImplementedError


@dataclass(frozen=True)
class Circle(Shape):
    radius: float = 1.0

    def area(self) -> float:
        return math.pi * self.radius ** 2


@dataclass(frozen=True)
class Square(Shape):
    side: float = 1.0

    def area(self) -> float:
        return self.side ** 2


# Ćw. 9 - porównanie dataclass vs NamedTuple vs TypedDict
@dataclass
class Point3D_DC:
    x: float
    y: float
    z: float


class Point3D_NT(NamedTuple):
    x: float
    y: float
    z: float


class Point3D_TD(TypedDict):
    x: float
    y: float
    z: float
