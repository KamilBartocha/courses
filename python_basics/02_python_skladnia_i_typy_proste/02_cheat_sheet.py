name = "Alice"
age = 25

print("Imię: " + name)
print("Imię: {}".format(name))
print(f"Imię: {name}, wiek: {age}")

counter = 0
price = 19.99
counter += 1
price *= 1.23
print(counter, f"{price:.2f}")

print(type(42), type(3.14), type(True), type('hello'), type([1, 2]), type({'a': 1}))

print(3 + 2, 5 / 2, 5 // 2, 5 % 2, 2 ** 8)
print(3 + 5 * 0.5, (3 + 5) * 0.5)

x = 5
print(x == 5, x != 5, x > 3, x >= 5)
print(not True, True and False, True or False)

age = 20
print(age >= 18 and True)
print(0 or 'default')

a, b = 5, 7
a, b = b, a
print(f'a={a}, b={b}')

print(bool(0), bool(''), bool([]), bool(42))

x = None
print(x, type(x))

scores = {'Alice': 95}
print(scores.get('Bob'), scores.get('Bob', 0))

print(isinstance(42, int), isinstance(True, int), isinstance(True, bool))

def show_type(x):
    if isinstance(x, (int, float)):
        print(f"{x} to liczba")
    elif isinstance(x, str):
        print(f"{x!r} to napis")

show_type(42)
show_type("hello")

print(float(7), int(3.99), round(3.99))
print(int('42'), 'Age: ' + str(25))

word = "Python"
print(word[0], word[-1], word[0:2], word[::-1], len(word))
print("J" + word[1:])

text = 'Hello, World!'
print(text.upper(), text.lower())
print(text.replace('o', '0'))
print(text.count('l'), text.split(', '), text.startswith('Hello'))
print('   python   '.strip())
print("Linia 1\nLinia 2", "Kol 1\tKol 2")
print(r"C:\Users\name")
print("-" * 30)
