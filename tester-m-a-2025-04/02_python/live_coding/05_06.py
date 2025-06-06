import os

# 05.06.2025

file = open("02_python/008_python_pliki_i_moduly/008_file_text.txt", "r", encoding='UTF-8')
content = file.read()
file.close()



file = open("02_python/008_python_pliki_i_moduly/008_file_text.txt", "r", encoding='UTF-8')
line = file.readline()
line2 = file.readline()
line3 = file.readline()
line4 = file.readline()
line5 = file.readline()
line6 = file.readline()



file.close()

# print(line)
# print(line2)
# print(line3)
# print(line4)

# print(f">{line5}<")


file = open("02_python/008_python_pliki_i_moduly/008_file_text.txt", "r", encoding='UTF-8')
content = file.readlines()
file.close()

# print(content)

# print(content[3])   # 4 linia



file = open("02_python/008_python_pliki_i_moduly/008_file_text.txt", "r", encoding='UTF-8')
linie_pliku = file.readlines()
file.close()

# print(linie_pliku)

# print(linie_pliku[3])   # 4 linia




file = open("02_python/008_python_pliki_i_moduly/008_file_text.txt", "r", encoding='UTF-8')
interator = 1
for el in file:
    # print(interator, el)
    interator += 1

file.close()






# f = open("02_python/008_python_pliki_i_moduly/plik_tmp.txt", "w")
# f.write("ala ma kota")
# f.write("ala ma kota 2")
# f.close()



f = open("02_python/008_python_pliki_i_moduly/plik_tmp2.txt", "a")
f.write("ala ma kota\n")
f.close()




file = open("02_python/008_python_pliki_i_moduly/008_file_text.txt", "r", encoding='UTF-8')
content = file.read()
print(content)
file.close()






with open("02_python/008_python_pliki_i_moduly/008_file_text.txt", "r", encoding='UTF-8') as file:
    content = file.read()
    print(content)





with open("02_python/file_tmp.txt", "w") as zapisz_plik:
    zapisz_plik.write("plik za pomocą with!\n\n")
    zapisz_plik.write("koniec pliku")





with open("02_python/live_coding/05_06.py", "r", encoding='UTF-8') as file:
    content_file = file.read()
    print(content_file)


# with open("02_python/live_coding/05_06.py", "a", encoding='UTF-8') as file:
#     file.write("#haker!")#haker!



print(120 * "-")


# import math

# print(math.sqrt(9))

# import time

# print(1)
# time.sleep(5)
# print(2)


# import math

# print(math.sqrt(9))


# import math as m

# print(m.sqrt(9))



# import os
# print(os.system("ls"))


# from math import sqrt, sin

# # math.sqrt() nie wolno
# print(sqrt(10))



# from math import *

# sqrt()
# sin()
# cos()



# import time
# import time as t
# from time import time
# from time import *



# import selenium
# import pytest






# 009

def add(x, y):
    return x + y


add2 = lambda x1, y1: x1  + y1

print(add2(1, 2))







# *
# def return_last(x):
#     return x[-1]



# lista1 = [(1, 2), (2, 1), (0, 4)]

# lista2 = sorted(lista1, key=return_last)
# print(lista2)



lista1 = [(1, 2), (2, 1), (0, 4)]

lista2 = sorted(lista1, key=lambda x: x[-1])
print(lista2)









szesciany = []
for x in range(10):
    szesciany.append(x ** 3)

print(szesciany)

szesciany2 = [x ** 3 for x in range(10)]
print(szesciany2)




kwadraty = [el ** 2 for el in range(1, 102) if el % 2 != 0]
print(kwadraty)


even = [number for number in range(1, 101) if number % 2 == 0]
print(even)





x = -3
y = 3

print(abs(x))
print(abs(y))




nums = [2, 4, -6, -9, 11, -12, 14, -5, 17]

# x = [number for number in nums if number < 0]
# y = sum(x)
# z = abs(y)
# print(x)
# print(y)
# print(z)


print(abs(sum([number for number in nums if number < 0])))





zbior = {znak for znak in "abracadabra" if znak not in "abc"}
print(zbior)



tekst = "google.com"
wystapienia = {znak: tekst.count(znak) for znak in tekst}
print(wystapienia)




szesciany3 = (x ** 3 for x in range(10))  # yield - generator
print(szesciany3)











class Payment:
    amount = 0
    is_done = True

    def show_amount(self):
        print(f"alamakota {self.amount}")

    def who_am_i(self):
        print("To klasa Payment")

    def sort(self):
        pass



p1 = Payment()

print(p1.is_done)
print(p1.amount)

p1.amount = 100

p1.show_amount()
p1.who_am_i()




def len(x):
    pass


lista1 = [1, 2]

lista1.append(3)

len(lista1)









class TxtFile:
    path = "1.txt"
    def read_file(self):
        with open(self.path) as f:
            return f.read()

    def write_file():
        pass




txt1 = TxtFile()
content = txt1.read_file()
print(content)

lista1 = [2, 1]
lista1.sort().append(3)
