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
