# 31.05.2025

def new_section():
    print("Koniec sekcji")
    print("-" * 140)
    print("Nowa sekcja")

lista1 = [1, 2, 3, 4, 1, 2]
lista1.remove(2)
print(lista1)

lista1 = [1, 2, 3, 4, 1, 2, "ala", "ma"]
var = lista1.pop()
print(lista1)
print(var)

lista1.insert(1, "zebra")
print(lista1)

lista1.extend(["33", 33])
print(lista1)

len2 = lista1.count(2)
print("count")
print(len2)

idx33 = lista1.index(2)
print(idx33)

lista2 = [2, 4, 5, 7, 2, 4, 1, 5.1, 5.0]
lista2.sort()

print(lista2)


list3 = [1, 1, 1, 2, 1, 2, 1, 1]

print(list3.count(1))


list3 = [1, 1, "1", 2, "1", 2, 1, 1]

print(list3.count("1"))

print("metody na liście^")
print("-" * 120)



new_section()


lista4 = [1, 2, 4, 1, 5]

# lista4.len() nie wolno
print(len(lista4))
lista_5 = list(reversed(lista4))
print(lista_5)




list_sorted = sorted(lista4)
print(list_sorted)








lista6 = [6, 4, 1, 2, 1, 9, 2]
lista6.sort()
print(lista6)





lista7 = [6, 4, 1, 2, 1, 9, 2]
lista7_sorted = sorted(lista7)  #lista7 nie jest zmieniona
print(lista7_sorted)

new_section()

print("Słowniki")
print(("-" * 120))


dict_1 = {1: "ala", 2: "ma", 3: "kota"}
print(dict_1)

print(dict_1[2])

dict_1[4] = "zebra"
print(dict_1)
print(type(dict_1))



# .keys()
# .values()
# .items()

x = dict_1.keys()
print(x)

y = dict_1.values()
print(y)

z = dict_1.items()
print(z)



zbior = {"ala", "kot", 1, 2.89, 1, 1}
print(zbior)

print("ala" in zbior)








lista2 = [22, 2, 25 ,1 ,2 ,3, 5 ,3, 1, 10, 13]
x = list(set(lista2))
print(x)

print("Koniec sekcji")
print("-" * 120)
print("Nowa sekcja")


###
zbior = {"ala", "kot", 1, 2.89, 1, 1}
zbior.add("ma")
print(zbior)
zbior.update(["masdasdsada", "maaaaa"])
print(zbior)
zbior.remove("ala")
print(zbior)

pay1_response = [12, 13, 14, 15]
pay2_response = [13, 14, 15, 16, 17]
pay3_response = [11, 13, 14, 18, 20]

result = list(set(pay1_response) & set(pay2_response) & set(pay3_response)) #{13, 14}
print(result)


# list = 23   # nie wolno
# tuple
tokens = (21312313, 32423424294)
print(tokens[1])

new_section()


# i = 3
# i = 5

age = 44

print("Wiek")
print(age)


#1
print("wiek:", age)
print("Masz " + str(age) + " lata.")    # konkatenacja ze zmianą typu
print("Masz {} lata.".format(age))
print(f"Masz {age / 2} lata!")


# len()
# .sort()





x1 = 10
x2 = 20

print(x1 ** x2)


print(x1 != x2)




temp = 10


if temp > 25:
    print("jest ciepło")
else:
    print("jest zimno")
    print("jest zimno2")
print("ala ma kota")

new_section()

i = 20
print(i.bit_length())


#ad4

x = 10
print(not x > 9)   # -> x jest większe od 9, -> True, ale not zmienia na
                   # przeciwieństwo -> False









# imie = input("Podaj imię: ")

# ostatnia_litera = imie[-1]

# if ostatnia_litera == "a":
#     print("K")
# else:
#     print("M")









response_http = 600

if response_http >= 200 and response_http < 300:
    print("Success")
elif response_http >= 300 and response_http < 400:
    print("Redirected")
elif response_http >= 400 and response_http < 500:
    print("Error")
else:
    print("Pozostałe kody - niewiadomo")








# imie = input("Podaj imię: ")

# ostatnia_litera = imie[-1]

# if ostatnia_litera == "a":
#     print("K")
# else:
#     print("M")



# print("K") if ostatnia_litera == "a" else print("M")



punkty = 40
x = "Zdałeś" if punkty >= 50 else "Nie zdałeś"

print(x)






payments = [21]

is_payments_empty = True if len(payments) == 0 else False

print(f"Czy lista jest pusta? {is_payments_empty}")



# print("Hello World!")
# print("Hello World!")
# print("Hello World!")
# print("Hello World!")
# print("Hello World!")
# print("Hello World!")


for i in range(10):
    print("Hello World!")





for el in [1, 2, 3, 12]:
    kwadrat = el ** 2
    print(kwadrat)


lista10 = [1, 2, 1, 2, 3, 5, 7, 89]

for number in lista10:
    print(number * 10)




print("Ala ma kota")


# y = 1
# x = "101010" * 200
# while y > 0:
#     print(x)



# lines = list()
# print('Wprowadź tekst po linijce.')
# print('Żeby zakończyć wprowadź pustą linię.')
# line = input('Następna linijka: ')
# while line != '':
#     lines.append(line)
#     line = input('Następna linijka: ')
# print(lines)










lista11 = ["ala", "ma", 1, 2, 4, 6, "kota"]


lista_liczby = []

for el in lista11:
    if type(el) == int or type(el) == float:
        lista_liczby.append(el)

print(lista_liczby)


lista_liczby_2 = []

for el in lista11:
    if type(el) != int:
        continue
    lista_liczby_2.append(el)

print(lista_liczby_2)


lista11 = ["ala", "ma", 1, 2, 4, 6, "kota"]

for el in lista11:
    if el == "ma":
        break
    print(el)







def print_hello():
    print("hello")
    print("funkcja print_hello")
    print("koniec_funkcji")
print("po funkcji")

print_hello()


new_section()









def add_2_2():
    print(2 + 2)

add_2_2()



new_section()



def sum3_3():
    return 3 + 3


x = sum3_3()
print(x)







def add(x, y):
    """ALA MA KOTAAdds 2 values x and y, should be int or float
        x: value 1
        y: value 2
    return: sum x + y """
    print(f"x: {x}")
    print(f"y: {y}")
    result = x + y
    return result


add_result1 = add(20, 333)
add_result2 = add(20, 3)
add_result3 = add(20, 0)

# 353
# 23
# 20
print(add_result1)
print(add_result2)
print(add_result3)









def add(x, y, z=0):
    print(f"x: {x}")
    print(f"y: {y}")
    print(f"z: {z}")

    result = x + y + z
    return result

res1 = add(1, 2)
res2 = add(1, 2, 7)

print(res1)
print(res2)





