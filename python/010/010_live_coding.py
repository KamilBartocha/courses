"""
PLAN:
DONE 9:00  - 10:20 009 - Programowanie funkcyjne cz1
DONE 10:20 - 10:35 przerwa 15 min
DONE 10:35 - 12:00 009 - Programowanie funkcyjne cz2

DONE 12:00 - 12:30 przerwa obiadowa 30 min

DONE 12:30 - 13:50 010 - Programowanie obiektowe cz1
DONE 13:50 - 14:05 przerwa 15 min
14:05 - 15:30 010 - Programowanie obiektowe cz2

"""

class Animal:
    kind = "dogs"
    def  __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def set_name(self, new_name):
        self.name = new_name


dog1 = Animal("Burek", 4)
dog2 = Animal("Fado", 4)
print(id(dog1))
print(id(dog2))

x = 4
y = 4

lst1 = [1, 2]
lst2 = [1, 2]

print(id(lst1))
print(id(lst2))

# print(id(x))
# print(id(y))

# print(type(dog1))
# print(dog1.kind)
# print(dog2.name)
# print(dog1.age)

# print(dog1.get_age())

# print(dog2.get_name())
# dog2.set_name("Reksio")
# print(dog2.get_name())
# dog2.name = "Fado2"
# print(dog2.get_name())

# print(dog2.kind)
# dog2.kind = "parrot"
# print(dog2.kind)





