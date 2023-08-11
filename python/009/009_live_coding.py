"""
PLAN:
9:00  - 10:20 009 - Programowanie funkcyjne cz1
10:20 - 10:35 przerwa 15 min
10:35 - 12:00 009 - Programowanie funkcyjne cz2

12:00 - 12:30 przerwa obiadowa 30 min

12:30 - 13:50 010 - Programowanie obiektowe cz1
13:50 - 14:05 przerwa 15 min
14:05 - 15:30 010 - Programowanie obiektowe cz2

"""
# import numpy as np

# np.array()

# def funk1(x, y, z):
#     x = x * 5
#     result = x + y + z
#     return(result)

# def funk2(x, y, z):
#     """Funkcyjne"""
#     return(x + y + z)

# war = funk1(1, 2 , 3)



# adding = lambda x, y, z: x + y * z
# print(adding(2, 3, 4))
# value = adding(3, 4, 6)
# print(f"value: {value}\n")
# print(value)

# |
# |
# |
# |
# -------------
# a = 2, b = 3
#
# pitagoras = lambda a, b: ((a * a) + (b * b)) ** 0.5
# from math import sqrt
# # pitagoras = lambda a, b: sqrt((a * a) + (b * b))
# slowo = "pot"
# print(slowo.startswith("p"))

# starts_with_sing = lambda word, sign: word.startswith(sign.lower()) or word.startswith(sign.upper())
# word = "kot"
# sign = "p"
# print(starts_with_sing(word, sign))

# import datetime
# now = datetime.datetime.now()
# print(now.year)

# x = "4.33242"
# print(x.isdigit())



# temperatury = [
#     37.6, 35.8, 37.6, 33.4, 34.1, 37.1, 35.9, 34.1, 37.1, 40.5, 38.5, 37.6,
#     35.8, 34.5, 36.4, 38.3, 37.5, 37.7, 34.0, 35.3, 35.7, 38.9, 34.8, 34.1,
#     39.6, 35.4, 34.7, 37.6, 38.4, 36.4, 39.8, 39.1, 37.1, 35.6, 36.8, 37.6,
#     36.7, 40.0, 38.0, 34.1, 35.5, 38.5, 36.1, 32.6, 32.9, 34.5, 41.0, 38.3,
#     33.7, 38.7, 36.9, 36.2, 33.7, 38.3, 35.3, 38.3, 40.1, 39.3, 38.2, 37.6,
#     39.1, 37.1, 34.4, 38.7, 35.8, 38.2, 38.2, 33.1, 37.8, 36.5, 37.6, 37.4,
#     34.3, 37.7, 36.0, 37.5, 37.6, 36.5, 31.3, 37.7, 40.3, 39.5, 35.7, 38.1,
#     34.7, 36.5, 34.3, 38.0, 37.0, 38.5, 39.4, 37.6, 41.7, 40.0, 38.4, 38.9,
#     34.2, 40.2, 34.3, 35.3
# ]
# wynik = list(filter(lambda x: x>=40.0,  temperatury))
# print(wynik)

# texts = ["php", "w3rr3w", "Python", "abcd", "Java", "aaa"]

# # x = "\n"
# # print(x.isspace())

# sample_names = ['antoni', 'Jakub', 'zuzanna', 'Julia', 'Jan', 'szymon']
# names = list(filter(lambda x: not x[0].islower(), sample_names))


# x = -1.1000000000000014
# print(round(x,3))



# from functools import reduce
# nums = [1, 2, 3, 4, 5]

# print(reduce(lambda a, b: a * b if a>3 else 2, nums))
# a = 5

# if a > 3:
#     print(True)
# else:
#     print(False)

# print(True) if a > 3 else print(False)

# szesciany = []
# for x in range(10):
#     szesciany.append(x**3)

# szesciany2 = [x**3 for x in range(10)]

# print(szesciany)
# print(szesciany2)

# str1 = "sdf 23 safs8 5 sdfsd8 sdfs 56 21sfs 20 5"

