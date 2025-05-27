# import math
from math import sqrt
"""
### Ćwiczenie nr 6:

Napisz funkcję w Pythonie, która zlicza liczbę znaków (częstotliwość znaków) w ciągu.

Przykładowy ciąg: `google.com`

Oczekiwany wynik:

`{'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}`"""

text = "google.com"


def count_signs(text):
    result = {}
    for sign in text:
        if sign not in result.keys():
            result[sign] = 1
        else:
            result[sign] += 1
    return result

# print(count_signs(text))




# file = open("02_python/008_file_text.txt", "r", encoding="UTF-8")
# file = open("02_python/008_file_text.txt", "r")

# content = file.read()

# content = file.readline()
# # file.seek(0)
# content2 = file.readline()

# # content = file.readlines()

# print(content)
# print(content2)

# file.close()






f = open("alamakota.txt", "w")

f.write("hello world")
# f.read()
f.close()



# f = open("alamakota.txt", "a")

# f.write("hello world\n")

# f.close()



# name = "alamakota.txt"



# with open(name, "r") as f1:
#     print(f1.read())

# f1.read()



# with open("02_python/tmp_04_24.py", "r") as file:
#     x = file.read()
#     print(x)





# x = math.sqrt(10)
# x = sqrt(10)

# print(x)

# import os

# x = os.system("ls")
# print(x)


# import math
# math.xxxx()

# from math import xxx
# from math import acos, sin, sqrt


from math import *   # -> sqrt
import math          # -> math.sqrt()




from time import sleep

print("x")

# sleep(10)

print("y")

# import os
# os.system("pip install -r req.txt")



# my_func = lambda x, y: x ** y

# print(my_func(2, 3))


# def return_last(var):
#     return var[-1]


list1 = [[9, 2], [2, 3], [4, 1], [8, 0]]


# list2 = sorted(list1, key=return_last)
list2 = sorted(list1, key=lambda var: var[-1])

print(list2)



szesciany = []
for x in range(10):
    szesciany.append(x ** 3)

print(szesciany)


szesciany2 = [x ** 3 for x in range(10)]
print(szesciany2)



parz = [number for number in range(0, 101, 2)]
print(parz)




parz = [x ** 2 for x in range(100) if x % 2 == 0]
print(parz)