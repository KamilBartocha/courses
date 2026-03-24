# Solutions: 101_python_interm_oop_advanced.ipynb
##############################################################################
# 1. Rectangle
##############################################################################

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


rect = Rectangle(5, 3)
print(rect.area())       # 15
print(rect.perimeter())  # 16

##############################################################################
# 2. Book
##############################################################################

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def get_info(self):
        return f"'{self.title}' by {self.author}, published in {self.year}"


book = Book("1984", "George Orwell", 1949)
print(book.get_info())
# '1984' by George Orwell, published in 1949

##############################################################################
# 3. ShoppingCart
##############################################################################

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, name, price):
        self.items.append({"name": name, "price": price})

    def remove_item(self, name):
        for item in self.items:
            if item["name"] == name:
                self.items.remove(item)
                return
        print(f"{name} not found in cart.")

    def total(self):
        return sum(item["price"] for item in self.items)


cart = ShoppingCart()
cart.add_item("Laptop", 1999)
cart.add_item("Mouse", 25)
print(cart.total())       # 2024
cart.remove_item("Mouse")
print(cart.total())       # 1999

##############################################################################
# 4. Animal + Dog
##############################################################################

class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        return "Some generic animal sound"

    def __str__(self):
        return f"Animal(name: '{self.name}')"


class Dog(Animal):
    def make_sound(self):
        return "Woof! Woof!"

    def __str__(self):
        return f"Dog(name: '{self.name}')"


dog = Dog("Rex")
print(dog)               # Dog(name: 'Rex')
print(dog.make_sound())  # Woof! Woof!

##############################################################################
# 5. Shape + Circle + Rectangle
##############################################################################

import math


class Shape:
    def area(self):
        raise NotImplementedError("Subclass must implement area()")


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


circle = Circle(3)
rect = Rectangle(4, 5)
print(f"Circle area: {circle.area():.2f}")    # 28.27
print(f"Rectangle area: {rect.area()}")       # 20

##############################################################################
# 6. Employee + Manager
##############################################################################

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"Employee(name: '{self.name}', salary: {self.salary})"


class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department
        self.team = []

    def add_to_team(self, employee):
        self.team.append(employee)

    def __str__(self):
        members = len(self.team)
        return (
            f"Manager(name: '{self.name}', salary: {self.salary}, "
            f"department: '{self.department}', team size: {members})"
        )


emp = Employee("Bob", 5000)
mgr = Manager("Alice", 8000, "Engineering")
mgr.add_to_team(emp)
print(emp)
print(mgr)
print(Manager.__mro__)

##############################################################################
# 7. Thermometer
##############################################################################

class Thermometer:
    def __init__(self, celsius):
        self.__celsius = celsius

    def get_temp(self):
        return self.__celsius

    def set_temp(self, value):
        if value < -273.15:
            print("Invalid temperature.")
        else:
            self.__celsius = value


t = Thermometer(20)
print(t.get_temp())   # 20
t.set_temp(37)
print(t.get_temp())   # 37
t.set_temp(-300)      # Invalid temperature.
print(t.get_temp())   # 37

##############################################################################
# 8. SecureCounter
##############################################################################

class SecureCounter:
    def __init__(self):
        self.__count = 0

    def increment(self):
        self.__count += 1

    def decrement(self):
        if self.__count > 0:
            self.__count -= 1

    def reset(self):
        self.__count = 0

    def get_count(self):
        return self.__count


counter = SecureCounter()
counter.increment()
counter.increment()
counter.increment()
print(counter.get_count())   # 3
counter.decrement()
print(counter.get_count())   # 2
counter.reset()
print(counter.get_count())   # 0
counter.decrement()
print(counter.get_count())   # 0 (not negative)

##############################################################################
# 9. Person z walidacją
##############################################################################

class Person:
    def __init__(self, name, age):
        self.__name = None
        self.__age = None
        self.set_name(name)
        self.set_age(age)

    def get_name(self):
        return self.__name

    def set_name(self, value):
        if not value:
            print("Invalid name.")
        else:
            self.__name = value

    def get_age(self):
        return self.__age

    def set_age(self, value):
        if not (0 <= value <= 150):
            print("Invalid age.")
        else:
            self.__age = value


p = Person("Alice", 30)
print(p.get_name())   # Alice
print(p.get_age())    # 30
p.set_age(200)        # Invalid age.
p.set_name("")        # Invalid name.
print(p.get_age())    # 30

##############################################################################
# 10. Point
##############################################################################

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False


p1 = Point(1, 2)
p2 = Point(1, 2)
p3 = Point(3, 4)
print(p1)           # Point(1, 2)
print(repr(p1))     # Point(x=1, y=2)
print(p1 == p2)     # True
print(p1 == p3)     # False

##############################################################################
# 11. Fraction
##############################################################################

class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __add__(self, other):
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)


f1 = Fraction(1, 2)
f2 = Fraction(1, 4)
f3 = f1 + f2
print(f1)   # 1/2
print(f2)   # 1/4
print(f3)   # 6/8

##############################################################################
# 12. Bag
##############################################################################

class Bag:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def __len__(self):
        return len(self.items)

    def __add__(self, other):
        new_bag = Bag()
        new_bag.items = self.items + other.items
        return new_bag

    def __str__(self):
        return "Bag: " + ", ".join(self.items)


bag1 = Bag()
bag1.add("apple")
bag1.add("banana")
bag2 = Bag()
bag2.add("cherry")
print(len(bag1))     # 2
bag3 = bag1 + bag2
print(len(bag3))     # 3
print(bag3)          # Bag: apple, banana, cherry

##############################################################################
# 13. Counter z metodą klasową
##############################################################################

class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

    @classmethod
    def get_count(cls):
        return cls.count

    @classmethod
    def reset_count(cls):
        cls.count = 0


c1 = Counter()
c2 = Counter()
c3 = Counter()
print(Counter.get_count())   # 3
Counter.reset_count()
print(Counter.get_count())   # 0

##############################################################################
# 14. Rectangle z factory method
##############################################################################

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    @classmethod
    def from_square(cls, side):
        return cls(side, side)


rect = Rectangle(4, 6)
square = Rectangle.from_square(5)
print(rect.area())                  # 24
print(square.area())                # 25
print(square.width, square.height)  # 5 5

##############################################################################
# 15. Pizza z factory methods
##############################################################################

class Pizza:
    def __init__(self, size, toppings):
        self.size = size
        self.toppings = toppings

    @classmethod
    def margherita(cls):
        return cls("M", ["tomato", "mozzarella"])

    @classmethod
    def pepperoni(cls):
        return cls("L", ["tomato", "mozzarella", "pepperoni"])

    def __str__(self):
        return f"Pizza {self.size}: {', '.join(self.toppings)}"


p1 = Pizza.margherita()
p2 = Pizza.pepperoni()
print(p1)   # Pizza M: tomato, mozzarella
print(p2)   # Pizza L: tomato, mozzarella, pepperoni
