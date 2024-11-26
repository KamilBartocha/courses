# 1
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def circumference(self):
        return 2 * math.pi * self.radius

# Przykład użycia:
circle = Circle(5)

print(f"Area: {circle.area()}")
print(f"Circumference: {circle.circumference()}")

# 2
##############################################################################


class Person:
    def __init__(self, name, age):
        """Inicjalizuje obiekt Person z imieniem i wiekiem."""
        self.name = name
        self.age = age

    def birthday(self):
        """Zwiększa wiek osoby o 1."""
        self.age += 1

    def __str__(self):
        """Zwraca czytelną reprezentację osoby."""
        return f"Person(name: '{self.name}', age: {self.age})"

person = Person("Alice", 30)
print(person)  # Wyświetla: Person(name: 'Alice', age: 30)

person.birthday()
print(person)  # Wyświetla: Person(name: 'Alice', age: 31)

# 3
##############################################################################

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            print(book)

library = Library()
library.add_book("1984 by George Orwell")
library.add_book("To Kill a Mockingbird by Harper Lee")

library.list_books()

# 4
##############################################################################


class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print("Some generic animal sound")

    def __str__(self):
        return f"Animal(name: '{self.name}')"

class Dog(Animal):
    def make_sound(self):
        print("Woof! Woof!")

    def __str__(self):
        return f"Dog(name: '{self.name}')"

dog = Dog("Rex")
print(dog)
dog.make_sound()


# 5
##############################################################################


import math

class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method.")

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

rectangle = Rectangle(4, 5)
circle = Circle(3)

print(f"Rectangle area: {rectangle.area()}")
print(f"Circle area: {circle.area()}")


# 6
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

    def __str__(self):
        return f"Manager(name: '{self.name}', salary: {self.salary}, department: '{self.department}')"

employee = Employee("John Doe", 7000)
manager = Manager("Jane Smith", 20000, "HR")

print(employee)
print(manager)
print(Manager.__mro__)
