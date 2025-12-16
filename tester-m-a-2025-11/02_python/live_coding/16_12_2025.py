# import math
list_endpoints = []

try:
    print("in try")
    result = 10/len(list_endpoints)
    print("end try")
except ZeroDivisionError:
    print("Coś poszło nie tak, nie udało się policzyć result")

print("hello")
print("program działa dalej")




list_endpoints = []

try:
    print("in try")
    result = 10/len(list_endpoints)
    print("end try")
except ZeroDivisionError as e:
    print("Coś poszło nie tak, nie udało się policzyć result")
    print(e)    # division by zero

print("hello")
print("program działa dalej")






print("-" * 120)
print("hello")
connection_db = 1
if connection_db == 0:
    raise Exception("Błąd! zero połączeń z bazą!!!")
print("po raise")



print("-" * 120)

list_endpoints = []

try:
    print("in try")
    result = 10/len(list_endpoints)
    print("end try")
except ZeroDivisionError:
    print("Coś poszło nie tak, nie udało się policzyć result")
else:
    print("nie ma wyjątków !")
finally:
    print("program działa dalej")

print("hello")





# try:
#     print(3/0)
#     print(x)
#     print(2 + "3")
# except ZeroDivisionError:
#     print("err1")
# except NameError:
#     print("err2")
# except Exception:
#     print("err3")


try:
    print(3/1)
    print("x")
    print(2 + "3")
except ZeroDivisionError:
    print("err1")
except NameError:
    print("err2")
except Exception:
    print("err3")
else:
    print("hi2")
finally:
    print("hi3")


print("-" * 120)
print("008")
print("-" * 120)




file = open("02_python/008_python_pliki_i_moduly/008_file_text.txt", "r", encoding='UTF-8')
print(file)

x1 = file.read()
print(x1)

# x1 = file.readline()
# print(x1)

# x1 = file.readlines()
# print(x1)

# for l in file:
#     print(l)


file.close()




# f = open("02_python/008_python_pliki_i_moduly/1.txt", "w")

# f.write("Ala ma kota")

# f.close()

f = open("02_python/008_python_pliki_i_moduly/2.txt", "a")

f.write("Ala ma kota\n\n")


f.close()


with open("02_python/008_python_pliki_i_moduly/008_file_text.txt", "r", encoding='UTF-8') as file:
    print(file.read())



# import math

# print(math.pi)
# print(math.sin(1))

# from math import pi, sin

# print(pi)
# print(sin(1))

import math as m

m.pi
m.cos(1)