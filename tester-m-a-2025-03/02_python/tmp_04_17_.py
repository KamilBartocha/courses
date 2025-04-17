def oddziel_zadania1():
    print("\n\n")
    print("Kolejna sekcja zadań:")
    print("*" * 120)
    print("-" * 120)

# list
list1 = [1, 20, 3]
list1.append(10)
print(list1)
list1.sort()
print(list1)

list1[0] = 100
print(list1)

# tuple - krotka

x = (1, 3, 4, 5)
print(x)
# x[0] = 100 #!!! nie wolno,


# słownik - dict

y = {1 : "ala", 2 : "ma", 3 : "kota"}

print(y[1])
print(list(y.keys()))
print(y.values())

y[5] = "alamakota"
print(y)

# set - zbiór

z = {1, 2, 3, 4, 1, 2}
print(z)
z.add(10)
print(z)

lista2 = [1, 2, 3, 1, 2, 1, 4, 6, 7, 1, 0]

lista2 = list(set(lista2))
print(lista2)

oddziel_zadania1()

#if-else

# is_list2_empty = len(lista2) == 0  # True if lista2 = []

if len(lista2) > 0:
    lista3 = sorted(lista2, reverse=True)
    print(lista3)
else:
    print("Nie można posortować, pusta lista!")


rest_html_code = 350

if rest_html_code >= 200 and rest_html_code < 300:
    print("request with code 2xx")
elif rest_html_code >= 300 and rest_html_code < 400:
    print("request with code 3xx")
elif rest_html_code >= 400 and rest_html_code < 500:
    print("request with code 4xx")
else:
    print("request unknown: < 200 and >= 500")

print("alamakota")

oddziel_zadania1()
#for

for i in range(10):
    print("hello")

for el in lista2:
    print(f"Element: {el}, lista: {lista2}")

lista4 = []
for x in lista2:
    double = x * 3
    lista4.append(double)

print(lista4)


lista5 = [-1, 2, -3, 1, -7, 10, 100]

lista_dodatnie = []
lista_ujemene = []

for number in lista5:
    if number > 0:
        lista_dodatnie.append(number)
    elif number < 0:
        lista_ujemene.append(number)

print(lista_dodatnie)
print(lista_ujemene)
oddziel_zadania1()

x = 10
while x > 0:
    print(x)
    x = x - 1












# lines = []
# print('Wprowadź tekst po linijce.')
# print('Żeby zakończyć wprowadź pustą linię.')
# line = input('Następna linijka: ')

# while line != '':
#     lines.append(line)
#     line = input('Następna linijka: ')
# print(lines)





oddziel_zadania1()

liczby = list()
i = 2
while i < 101:
    print(i)
    liczby.append(i)
    print(liczby)
    i += 2


list6 = []
for i in range(2, 101, 2):
    list6.append(i)

print("*" * 100)
print(list6)

list7 = []
x = 2
for i in range(50):
    list7.append(x)
    x += 2


print("*" * 100)
print(list7)




for val in "string":
    if val == "i":
        continue
    print(val)

print("Koniec")

for i in range(100000000):
    pass


oddziel_zadania1()

# ### Ćwiczenie nr 2:
# Napisz program, który:
# Wypisze `True`, jeśli oba stwierdzenia są prawdziwe

# `x > 3` i `x < 10`


x = 20
if x > 3 and x < 10:
    print("True")


# ### Ćwiczenie nr 4:
# Napisz program, który:
# Odwróci wynik, wydrukuj `False`, jeśli wynik jest prawdziwy

# nie ( `x > 3` i `x < 10` )

x = 5

if not (x > 3 and x < 10):
    print("True")
else:
    print("False")



### Ćwiczenie nr 6:
# Napisz program, w którym:
# * Przypisz `8` do zmiennej `x` i `15` do zmiennej `y`
# * Utwórz 2 instrukcje warunkowe
# * Niech pierwsza wypisze: „Co najmniej jeden z warunków jest spełniony”,
#        jeśli `x` jest większe niż `3` lub `y` jest parzyste
# * Niech drugi wypisze „Żaden warunek nie jest spełniony”,
#       jeśli `x` jest mniejsze lub równe `3`, a `y` jest nieparzyste

x = 8
y = 15

if x > 3 or y % 2 == 0:
    print("co najmniej jeden z warunków jest spełniony")
if x <= 3 and y % 2 == 1:
    print("Żaden warunek nie jest spełniony")



# ### Ćwiczenie nr 7:
# Napisz program, w którym:
# * Utwórz listę zawierającą imiona: prowadzącego oraz wszystkich osób uczestniczacych w kursie
# * Następnie ją posortuj alfabetycznie, oraz
# * Policz ile z osób na liście ma imię żeńskie
#     * W tym celu możesz sprawdzić czy imię kończy się na „`a`”


lista1 = ["Przemysław", "Michał", "Kamil", "Tomasz", "Yelyzaveta", "Piotr", "Jakub", "Maciej", "Maciej", "Jacek", "Aleksandra", "Agnieszka", "Dorota"]

lista1.sort()
counter = 0

for imie in lista1:
    if imie[-1] == "a":
        counter = counter + 1

print(counter)

counter1 = 0
for imie in lista1:
    if imie.endswith("a"):
        counter1 = counter1 + 1

print(counter1)








lista_end_a = []

for imie in lista1:
    if imie[-1] == "a":
        lista_end_a.append(imie)

counter = len(lista_end_a)
print(lista_end_a)
print(counter)










def oddziel_zadania():
    print("Kolejna sekcja zadań:")
    print("*" * 120)
    print("-" * 120)



def add_2_5():
    x = 2 + 5
    print(x)

add_2_5()


oddziel_zadania1()

def add_2_6():
    x = 2 + 6
    return x


value = add_2_6()  # value = 8
print(value)

oddziel_zadania()


def add():
    return 4 + 5    # rerurn 9

print(add())   # print(9)


oddziel_zadania()




def oddziel_zadania_pro(nr_zadania):
    print(f"Zadanie nr {nr_zadania}")
    print("-" * 120)



oddziel_zadania_pro(1)
oddziel_zadania_pro(2)
oddziel_zadania_pro(3)
oddziel_zadania_pro(100)
# oddziel_zadania_pro() # nie wolno!!!!


def add(v1, v2):
    print(f"v1: {v1}, v2: {v2}")
    result = v1 + v2
    print(f"result: {result}")
    return result

x = add(2, 30)
print(x)


oddziel_zadania_pro(0)

def add_3(x, y, z):
    result = x + y + z
    return result



r1 = add_3(0, 0,  0)
r2 = add_3(10, 11, 25)

print(r1)
print(r2)




print("alamakota")

oddziel_zadania_pro(0)


def add_pro(x=0, y=0):
    print(x)
    print(y)
    res = x + y
    return res



print(add_pro())
print(add_pro())
print(add_pro(50))

add_pro(x=10, y=30)

oddziel_zadania_pro(00)



def add_pro_plus(x=0, y=0, z=0):
    print("x", x)
    print("y", y)
    print("z", z)
    res = x + y + z
    return res




result = add_pro_plus(x=10, z=30)

print(result)
