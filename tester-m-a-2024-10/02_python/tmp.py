# counter = 4
# tekst = "Python "
# print(tekst * counter)
# print("-" * 60)
# print(tekst * counter)


# x = "Ala ma kota 'Burek'"
# y = "Ala ma kota \"Burek\""

# print(x)
# print(y)

# print("Ala \nma kota")
# print("\tAla ma kota")

# print(r"C:\Users\natalia")    # to mój kod print(sadasda)

# """mój kod
# jest  print(alsdladasda)
# super!"""


# '''mój kod
# jest  print(alsdladasda)
# super!'''


# var1 = input("Podaj tekst: ")

# print(var1 * 10)

# var1 = input("Podaj wiek: ")

# print(2024 - var1)


# imie = input("podaj imię: ")
# wiek = input("podaj wiek: ")

# print("Jesteś " + imie + " i masz " + wiek + " lat")

# matrix = [[1, 2, 3],
#           [4, 5, 6],
#           [7, 8, 9]]

# print(matrix)
# print(matrix[2][0])   # [x][y] - x=wiersz - 1, y=kolumna - 1

# # matrix[2] ->   [7, 8, 9]
# # matrix[2][0] -> 7
# print(matrix[1][1])



# * Biorąc pod uwagę 2 ciągi, `s1` i `s2` zwróć nowy ciąg złożony z pierwszego,
# środkowego i ostatniego znaku każdego ciągu wejściowego
# * Dane:
#   * `s1 = "America"`
#   * `s2 = "Japan"`
# * Oczekiwany wynik:\
# `AJrpan`  0 z s1, 0 z s2, sr z s1, sr z s2, -1 z s1, -1 z s2


# s1 = "America"
# s2 = "Japan"

# s1_mid_idx = len(s1) // 2
# s2_mid_idx = len(s2) // 2

# result = s1[0] + s2[0] + s1[s1_mid_idx] + s2[s2_mid_idx] + s1[-1] + s2[-1]
# print(result)

# 5
# * Utwórz listę zawierającą imiona wszystkich kursantów
# * Następnie ją posortuj alfabetycznie, oraz
# * Sprawdź ile elementów ona zawiera
# * wyświetl listę i jej długość

# kursanci = ['Monika', 'Andrzej', 'Damian', 'Joanna', 'Martyna']

# kursanci.sort()

# len_kursanci = len(kursanci)
# print(f"Lista: {kursanci}, długość: {len_kursanci}")


# kursanci = ['Monika', 'Andrzej', 'Damian', 'Joanna', 'Martyna']

# kursanci_sort = sorted(kursanci)

# len_kursanci = len(kursanci_sort)
# print(f"Lista: {kursanci_sort}, długość: {len_kursanci}")











# c = 20

# if c > 20:
#     print("jest ciepło")
# elif c > 0 and c <= 20:
#     print("Jest tak sobie")
# elif c > -5 and c <= 0:
#     print("jest trochę zimno")
# else:
#     print('jest zimno brrr')
# print("Ala ma kota")




# lista1 = [1, 2, 3]

# for element in lista1:
#     print(element ** 2)
#     print("koniec iteracji")
# print("koniec programu")


# txt = "Ala ma kota"

# for char in txt:
#     print(char * 10)

# tup = (1, 2, 3, 4)
# for num in tup:
#     print(num * 100)


# lista1 = []
# for el in range(0, 101, 2):
#     lista1.append(el)

# print(lista1)

# for _ in range(10):
#     print("hello")


# x = 0
# while x < 10:
#     print("hello")
#     x = x + 1

# lines = list()
# print('Wprowadź tekst po linijce.')
# print('Żeby zakończyć wprowadź pustą linię.')
# line = input('Następna linijka: ')
# while line != '':
#     lines.append(line)
#     line = input('Następna linijka: ')
# print(lines)


# for i in range(10):
#     pass
# print("Pętla wykonana")




# def print_ala_ma_kota():
#     """prints "ala ma kota" into console """
#     print("ala")
#     print("ma")
#     print("kota")


# print_ala_ma_kota()





# def print_msg(msg1, msg2="", msg3="domyślny"):
#     print(msg1)
#     print(msg2)
#     print(msg1)
#     print(msg3)


# print_msg("Ala ma psa", "ala")
# print("*" * 30)
# print_msg("Ala ma psa", "ala", "AAAAA")


def add3(var):
    result = var + 3
    return result

# # print(add3(5))
# var1 = add3(5)

# print(var1)

# try:
#     print(5 * (1 / 10))
# except ZeroDivisionError:
#     print("Nie wolno dzielić przez 0!!!")

# def add_vars_and_5(var1, var2=None):
#     if var2 == None:
#         return var1 + 5
#     elif var2 != None:
#         return var1 + var2 + 5

# x1 = add_vars_and_5(3)
# x2 = add_vars_and_5(3, 10)

# print(x1)
# print(x2)










# try:
#     var1 = int(input("1: "))
#     var2 = int(input("2: "))
#     result = var1 / var2
#     print(result)
# except ZeroDivisionError:
#     print("Nie wolno dzielić przez 0 ")
# except ValueError:
#     print("Coś poszło nie tak?")
# def policz():
#     var1 = int(input("1: "))
#     var2 = int(input("2: "))
#     result = var1 / var2
#     print(result)


# try:
#     policz()
# except Exception as error:
#     print(f"Coś poszło nie tak, błąd: {error}")
# else:
#     print("Nie było wyjąktów!")
# finally:
#     print("koniec bloku try-except")


# try:
#     policz()
# except Exception as error:
#     print(f"Coś poszło nie tak, błąd: {error}")
# else:
#     print("Nie było wyjąktów!")
# print("koniec bloku try-except")




# import sqlite3

# class DatabaseManager:
#     def __init__(self, db_name):
#         self.db_name = db_name
#         self.connection = None

#     def __enter__(self):
#         self.connection = sqlite3.connect(self.db_name)
#         return self.connection

#     def __exit__(self, exc_type, exc_val, exc_tb):
#         if exc_type != None:
#             if self.connection:
#                 self.connection.commit()
#                 self.connection.close()
#         return True   ## Do not use it. - pass for Exception

# with DatabaseManager('example.db') as conn:
#     cursor = conn.cursor()
#     cursor.execute('''CREATE TABLE IF NOT EXISTS users (
#                         id INTEGER PRIMARY KEY AUTOINCREMENT,
#                         name TEXT,
#                         age INTEGER
#                     )''')

#     cursor.execute('INSERT INTO users (name, age) VALUES (?, ?)', ("Jan", 30))
#     cursor.execute('INSE INTO users (name, age) VALUES (?, ?)', ("Anna", 25))
#     cursor.execute('SELECT * FROM users')
#     users = cursor.fetchall()
#     print(users)



# def test1():
#     raise Exception("test failed1")

# def test2():
#     raise Exception("test failed2")

# def test3():
#     raise Exception("test failed3")


# try:
#     test1()
#     test2()
#     test3()
# except Exception:
#     print("x")




# from time import sleep




# f = open(r'02_python/008_python_pliki_i_moduly/008_file_text.txt', 'r')
# content = f.read()
# print(type(content))

# content = f.readline()
# content2 = f.readline()

# content = f.readlines()

# for line in f:
    # print(line)

# print(len(f.readlines()))





# f.close()


# print(content)


# file = open(r'02_python/008_python_pliki_i_moduly/008_file_text2.txt', 'w')

# for i in range(1000):
#     file.write("Ala ma kota1\n")
# print(file.name)
# file.close()

# file = open(r'02_python/008_python_pliki_i_moduly/008_file_text3.txt', 'a')

# for i in range(1000):
#     file.write("Ala ma kota1\n")

# var1 = 2
# file.write(str(var1))

# file.close()


# f = open(r'02_python/008_python_pliki_i_moduly/008_file_text.txt', 'r')
# content = f.read()
# f.close()

# with open(r'02_python/008_python_pliki_i_moduly/008_file_text.txt', 'r') as x:
#     content = x.read()




# def longest_word(filename):
#     with open(filename, 'r') as infile:
#         words = infile.read().split()
#         print(words)
#         max = 0
#         for word in words:
#             if len(word) > max:
#                 max = len(word)
#                 words_max = []
#                 words_max.append(word)
#             elif len(word) == max:
#                 words_max.append(word)
#         return words_max

# print(longest_word('02_python/008_python_pliki_i_moduly/008_file_text.txt'))

# def longest_word(filename):
#     with open(filename, 'r') as infile:
#         words = infile.read().split()
#         words = sorted(words, key=len)
#         words = words[::-1]
#         result = [words[0]]
#         for idx, word in enumerate(words[1:]):
#             if len(words[idx]) > len(words[idx + 1]):
#                 break
#             result.append(word)
#         return result


# print(longest_word('02_python/008_python_pliki_i_moduly/008_file_text.txt'))

# import math

# x = math.sin(1)
# print(x)

# from math import sin, cos, sqrt

# x = sin(1)
# print(x)

# from math import *

# cos()
# sin()

# import math as m

# m.sin()
# m.cos()

import os
print(os.system("ls"))

