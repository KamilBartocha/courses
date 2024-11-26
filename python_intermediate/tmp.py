# class Samochod():
#     """doc"""
#     def __init__(self, marka, model, rok):
#         self.marka = marka
#         self.m = model

#     def opis(self):
#         x = 2023
#         return f"{self.marka} {self.m}, rok produkcji {x}"


# sam1 = Samochod("BMW", "1", 2005)

# print(sam1.marka)
# print(sam1.m)
# x = sam1.opis()
# print(x)
# y = Samochod("s", "t", 123)
# y.m


# class Zwierze:
#     def dzwiek(self):
#         print("not implemented for general Zwierze")

# class Pies(Zwierze):
#     def dzwiek(self):
#         return "Hau Hau"

# class Kot(Zwierze):
#     def dzwiek(self):
#         return "Miau"



# pies = Pies()
# kot = Kot()

# print(pies.dzwiek())
# print(kot.dzwiek())

# z = Zwierze()
# x = z.dzwiek()
# print(x)


# class KontoBankowe:
#     def __init__(self, wlasciciel, saldo):
#         self.wlasciciel = wlasciciel
#         self.__saldo = saldo  # Atrybut prywatny

#     def wplac(self, kwota):
#         if kwota > 0:
#             self.__saldo += kwota
#             print(f"Wpłacono {kwota}. Nowe saldo: {self.__saldo}")
#         else:
#             print("Kwota do wpłaty musi być większa niż 0.")
#     def sprawdz_saldo(self):
#         return f"Saldo konta: {self.__saldo}"


# konto1 = KontoBankowe("Jan Kowalski", 1000)
# konto1.wplac(500)               # Output: Wpłacono 500. Nowe saldo: 1500
# print(konto1.sprawdz_saldo())   # Output: Saldo konta: 1500

# # Próba dostępu do prywatnego atrybutu (powoduje błąd)
# # print(konto1.__saldo)
# # AttributeError: 'KontoBankowe' object has no attribute '__saldo'


# # class SuperError(Exception):
# #     def __init__(self, message, error_code=None):
# #         super().__init__(message)
# #         self.error_code = error_code

# #     def __str__(self):
# #         if self.error_code:
# #             return f"Error Code: {self.error_code}"
# #         else:
# #             return None

# # try:
# #     raise SuperError("Error", error_code=404)
# # except SuperError as e:
# #     print(f"Catch exception {e}")




# class A:
#     def __init__(self):
#         print("Inicjalizacja A")

#     def metoda_a(self):
#         print("Metoda z klasy A")

# class B(A):
#     def __init__(self):
#         super().__init__()  # Wywołanie konstruktora klasy A
#         print("Inicjalizacja B")

#     def metoda_b(self):
#         print("Metoda z klasy B")

# class C(B):
#     def __init__(self):
#         super().__init__()  # Wywołanie konstruktora klasy B
#         print("Inicjalizacja C")

#     def metoda_c(self):
#         print("Metoda z klasy C")

# # Przykład użycia:
# obiekt_c = C()
# obiekt_c.metoda_a()  # Output: Metoda z klasy A
# obiekt_c.metoda_b()  # Output: Metoda z klasy B
# obiekt_c.metoda_c()  # Output: Metoda z klasy C




# print(C.__mro__)


# class Home():
#     def __init__(self, x: int) -> None:
#         self.x = x

#     def __str__(self) -> str:
#         return f"value of x:{self.x}"

#     def __add__(self, other):
#         return Home(self.x + other)


# h1 = Home(3)
# h2 = Home(4)
# h3 = h1 + 5
# print(h3)





import math

class Shape:
    def area(self):
        raise NotImplementedError


class Ractangle(Shape):
    def __init__(self, a: float, b: float) -> None:
        self.a = a
        self.b = b

    def area(self) -> float:
        return self.a * self.b


class Circle(Shape):
    def __init__(self, r: float):
        self.r = r

    def area(self) -> float:
        return math.pi * self.r * self.r


rec: Ractangle = Ractangle(a=5, b=5.5)
circle: Circle = Circle(r=50)

print(rec.area())
print(circle.area())

class Employee:
    def __init__(self, name, salary) -> None:
        self.name = name
        self.salary = salary

    def __str__(self) -> str:
        return f"Employee: {self.name}, salary: {self.salary}"


class Manager(Employee):
    def __init__(self, name, salary, department) -> None:
        super().__init__(name, salary)
        self.department = department

    def __str__(self) -> str:
        return f"Employee: {self.name}, salary: {self.salary}, department: {self.department}"


e = Employee('Ala', 4000)
m = Manager('Basia', 10000, "HR")

print(e)
print(m)
print(Manager.__mro__)