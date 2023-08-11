int()
x = 4
y = 4
z = [1, 2]
v = z.copy()
print(id(x))
print(id(y))

print(id(z))
print(id(v))
z = list()


class Animal:

    type = "dog"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

