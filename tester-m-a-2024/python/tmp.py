# x = 5

# if x > 10:
#     print("większe od 10")
# elif x > 20:
#     print("większe od 20")
# else:
#     pass

# print("Ala ma kota") if x > 10 else print("nie ma kota")
# y = 20
# x = True if y > 100 else False



# def print_hello():
#     print("hello")
#     print("hello")


# print("przed")
# print_hello()
# print_hello()
# print_hello()
# print_hello()

# print("po")


# def print_welcome(name):
#     print(f'Witaj {name}!')



# print_welcome("Ala")


# def print_welcome(name):
#     print(f'Witaj {name}!')



# print_welcome(input("podaj imię: "))

# def add2(x):
#     y = x + 2
#     return y

# wynik = add2(10)

# print(wynik)


# def add3(x):
#     return x + 3

# wynik = add3(10)

# print(wynik)

# def add_two_numbers(x, y):
#     return x + y

# wynik = add_two_numbers(10, 20)

# print(wynik)


# def can_drive(age, is_sober):
#     if age > 18 and is_sober == True:
#         return "Yes"
#     else:
#         return "No"

# x = can_drive(19, True)
# print(x)

# y = can_drive(19, False)
# print(y)

# def generate_matrix(n, return_len=False):
#     print("zaczynam obliczenia")
#     result = []
#     for i in range(1, 11):
#         result.append(i * n)
#     print("Koniec obliczeń")
#     if return_len == True:
#         return result, len(result)
#     else:
#         return result


# tb3 = generate_matrix(3, True)
# tb4 = generate_matrix(4)


# print(tb3)
# print(tb4)


# lista = [1, 2, 3, 4, 5, 6, 7]

# def times_2():
#     y = 0
#     for i in lista:
#         lista[y] = lista[y] * 2
#         y = y + 1


# times_2()
# print(lista)


# lista = [1, 53, 32, 4, 6, 6, 7]

# def times_2():
#     for idx, val in enumerate(lista):
#         print(f'idx: {idx}')
#         print(f'value: {val}')
#         lista[idx] = val * 2


# times_2()
# print(lista)

# def duzo_parametrow(*args):
#     for i in args:
#         print(i)


# duzo_parametrow(1, 2, 3, 4, 5, 6, 7, 8, 9)






# x = "s"
# czy_jest_int = isinstance(x, int)
# print(czy_jest_int)




# wiek = input("podaj wiek:")
# is_int_or_float = isinstance(wiek, int)
# if is_int_or_float == True:
#     data_ur = 2024 - wiek
#     print(data_ur)
# else:
#     print("Wprowadziłeś złe dane, nie int i nie float")

# def calculate_sum(x):
#     if isinstance(x, list) or isinstance(x, tuple) or isinstance(x, set):
#         return sum(x)
#     else:
#         return f"Cannot calculate sum, given argument: {x} does not support sum"

# print(calculate_sum([2, 3 ,5]))
# print(calculate_sum((2, 3 ,50)))
# print(calculate_sum({2, 3 ,500}))

# print(calculate_sum(1))
# print(calculate_sum("Ala"))

# print("dalej")
# print("przed")

# try:
#     print(5 * (1/0))
# except ZeroDivisionError as e:
#     pass


# print("po bledzie")
""" +-- Exception
      +-- StopIteration
      +-- StopAsyncIteration
      +-- ArithmeticError
      |    +-- FloatingPointError
      |    +-- OverflowError
      |    +-- ZeroDivisionError
      +-- AssertionError
      +-- AttributeError
      +-- BufferError
      +-- EOFError
      +-- ImportError
           +-- ModuleNotFoundError
      +-- LookupError
      |    +-- IndexError
      |    +-- KeyError"""


# lista_err = []
# print("przed")

# try:
#     print(5 * (1/0))
# except ZeroDivisionError as e:
#     lista_err.append(e)
#     print(f"coś poszło nie tak")

# try:
#     print(5  + '5')

# except TypeError as e:
#     lista_err.append(e)
#     print(f"coś poszło nie tak")


# print(lista_err)
# print("po bledzie")



# lista_err = []
# print("przed")

# try:
#     print(5 * (1/0))
#     # print(5  + '5')
# except (ZeroDivisionError, TypeError) as e:
#     lista_err.append(e)
#     print(f"coś poszło nie tak")
# # except TypeError as e2:
# #     lista_err.append(e2)
# #     print(f"coś poszło nie tak")



# print(lista_err)
# print("po bledzie")








# wiek = input("podaj wiek:")
# is_str = isinstance(wiek, str)
# if is_str == True:
#     try:
#         wiek = int(wiek)
#     except ValueError as e:
#         print("nie udało się policzyć! wprowadzono nie-liczbę ValueError", e)
#     else:
#         data_ur = 2024 - wiek
#         print(data_ur)
#         print("jestem w else")
#     finally:
#         print("po wyjątkach")

# # 1) bez wyjątku -> try + else + finally
# # 2) wyjątek     -> except + finally

# print("po wyjątkach2")





# lista = []


# if len(lista) < 1:
#     raise Exception("Pusta lista z bazy danych nie można kontynuować!!!")

# pay1 = lista[0]


# print('x' +  2)
# print('x' +  2)

# print('x' +  2)

# lista = [1, 2, 3]
# lista.append(4)

# lista.append(9)

# a=True
# while a == True:
#     x = input("Podaj pierwsza liczbe: ")
#     y = input("Podaj druga liczbe: ")
#     try:
#         x2 = int(x)
#         y2 = int(y)
#     except Exception as e:
#      print(f"Błąd konwersji: '{e}'. Podaj liczby całkowite")
#     else:
#         print(f"Suma podanych liczb to: {x2+y2}")
#         a = False


# lista.append(9)
# print(lista)










# def add2(x ,y):
#     return x + y

# print(add2(3, 4))



# add2_func = lambda x, y: x + y

# print(add2_func(5, 6))


# def return_last(x):
#     return x[-1]



# lista = [(1, 2), (2, 1), (1, 4), (4, 2)]

# lista_sort = sorted(lista, key=return_last)
# print(lista_sort)


# lista = [(1, 2), (2, 1), (1, 4), (4, 2)]

# lista_sort = sorted(lista, key=lambda x: x[-1])
# print(lista_sort)








# lista = []

# for i in range(1, 11):
#     lista.append(i ** 2)

# print(lista)


# lista2 = [j ** 3 for j in range(1, 11)]
# print(lista2)


# lista = []

# for i in range(1, 11):
#     lista.append(i ** 2)

# print(lista)


# lista2 = [j ** 3 for j in range(1, 11) if j % 2 == 0]
# print(lista2)



even = [j for j in range(100) if j % 2 == 0]

print(even)