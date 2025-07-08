# 03.06.2025

#funckje



def super_funkcja():
    print("jest super")
    print("funkcje są wspaniałe")


# super_funkcja()    #wywołanie funkcji
# super_funkcja()    #wywołanie funkcji
# super_funkcja()    #wywołanie funkcji
# super_funkcja()    #wywołanie funkcji




def super_funkcja2(v1, v2, v3=0):
    """doc"""
    print("jest super")
    result = v1 + v2 + v3
    l1 = []
    l1.append(result)
    return l1

# print(super_funkcja2(1, 1 ,1))

# r1 = int(input("podaj"))
# x = super_funkcja2(r1, 3, 1)

# print(x)





# super_funkcja()    #wywołanie funkcji

# try:
#     print(4 * x)
# except NameError:
#     print("coś poszło nie tak - zmienna nie istnieje")
# except ZeroDivisionError:
#     print("coś poszło nie tak - dzielenie przez 0!")


# super_funkcja()    #wywołanie funkcji
# super_funkcja()    #wywołanie funkcji


# 007 wyjątki

# try:
#     print(4/0)
# except Exception as e:
#     print("coś poszło nie tak - zmienna nie istnieje")
#     print(e)



# try:
#     print(4 * x)
# except NameError:
#     print("coś poszło nie tak - zmienna nie istnieje")
# except ZeroDivisionError:
#     print("coś poszło nie tak - dzielenie przez 0!")






# while True:
#     x = input("podaj liczbę:")

#     try:
#         x_int = int(x)
#     except ValueError as er:
#         print("Konwersja się nie udała? Czy podałeś liczbę?", er)
#     else:
#         print(x_int)
#         break



# print("po wyjątkach")






#008 pliki

file = open("02_python/008_python_pliki_i_moduly/008_file_text.txt", "r", encoding='UTF-8')
content = file.read()
file.close()

print(content)
