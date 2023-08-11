# import math_op
# import pandas
# import matplotlib as mpl
# 1
import math_op
print(dir(math_op))
# result = return_sqrt(9)
# # 2
# import math_op
# result2 = math_op.return_sqrt

# # print(result)

# import os

# # print(os.system("pip install "))
# # print(os.system("pip install "))
# # os.mkdir("00_abcde")
# from time import sleep
# print("Dobranoc")
# sleep(2)
# print("Dzień dobry")

# import os.path
# print(os.path.curdir)













def nazwa_funk():
    print("hello")

nazwa_funk()

def nazwa_funk2(str1):
    print(str1)

nazwa_funk2("hello2")

def nazwa_funk_ale_zwraca():
    return "hello3"


x = nazwa_funk_ale_zwraca()
print(nazwa_funk_ale_zwraca())





def rev_list(list1):
    return list1[::-1]

lista = [1, 2, 4, 6]
lista4 = True

try:
    lista_odw = rev_list(lista)
    print(lista_odw)
except TypeError as err:
    print(f"Złapano wyjątek: {err}")
else:
    print("pirrwyszy element z listy:")
    print(lista_odw[0])
finally:
    print(type(lista))



err = "ERROR"
print(f"Złapano wyjątek: {err}")
print("Złapano wyjątek: " + err)
print("Złapano wyjątek: %s" % err)







try:
    f = open('text_tmp.txt', 'w', encoding='UTF-8')
    f.write("4\nnowa linia\n kolejna linia\n\tz tabulacją\n    4spacje\n")
    x = 42
    f.write(str(x))
except Exception:
    pass
else:
    f.close()


with open('text_tmp.txt', 'w', encoding='UTF-8') as f:
    f.write("4\nnowa linia\n kolejna linia")
    x = 42
    f.write(str(x))








f2 = open('text_tmp.txt', 'a')
f2.write("\nAppend_mode")
f2.close()






# Otwórz plik
fo = open("text.txt", "r")
print("Nazwa pliku: ", fo.name)

print(fo.tell())
fo.seek(0, 2)
line_position = fo.tell()
print(line_position)
# Zamknij otwarty plik
fo.close()















try:
    f = open('text.txt', 'r', encoding='UTF-8')
    content_list = f.readlines()
    print(content_list)
except FileNotFoundError:
    print("nie znaleziono pliku")
else:
    f.close()


# x = 2




# import math

# x = 1
# math.cos(x)

# import math as alamakota
# alamakota.sin()
# import math as m
# import pandas as pd


# from math import sin
# from math import cos

# y = sin(x)
# y = m.cos(x)

# from math import *









import os

print(os.system("ls"))

from time import *
print("przed")
sleep(10)
print("po")











