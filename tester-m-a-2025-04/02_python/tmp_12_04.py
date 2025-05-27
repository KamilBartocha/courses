x = 100

x = x + 1

print(x)

#################################
print("-" * 100)
y = 100

y = y - 1

print(y)

#################################
print("-" * 100)

n = 10

n += 1

print(n)
#################################
print("-" * 100)
ala = 9

print(ala)
#################################
print("-" * 100)

n0 = 5  # int

n1 = 3.5 # float

complex_value = 1 + 2j # complex num
#################################
print("-" * 100)
x = 30
y = 2.5

result = x * y

print(result)
#################################
print("-" * 100)


print("powiedział: 'Ala ma kota'")

print("powiedział: \"Ala ma kota\"")

print("powiedzi+/print()ał: \"Ala ma kota\"") # \ " '"

print("powiedział:\nAla ma kota")

print("powiedział:\tAla ma kota")

#################################
print("-" * 100)

print(90)   # wypisuję ile jeszcze minut do przerwy
x = 10
print(x)

"""
ten kod liczy szereg Ali, dla x=10
f(x) = ala ma kota
print(x)
"""
print("koniec")

'''
ten kod liczy szereg Ali, dla x=10
f(x) = ala ma kota
print(x)
'''
print("koniec")


kwota = 1000
lat = 3
proc = 8
result = (kwota * ((100 + proc) / 100) ** lat) #result = suma kwota + odsetki
print(result)

#################################
print("-" * 100)

x = "Ala ma kotadasdsadasdasdsad5"

znak = x[3]

print(znak)

znak_ostatni = x[-1]
print(znak_ostatni)

y = "Ala"
print(y)
# print(y[3]) Błąd !

#################################
print("-" * 100)

x = "Bartłomiej ma kota"

# imie = x[0] + x[1] + x[2]
# print(imie)

imie = x[0:-2]
print(imie)
print(x)

# ćwiczenie, wytnij "kota" ze zmiennej x
# x[start(włącznie):stop(wyłącznie)]
print(x[14:])
print(x[-4:])

imie = x[14:18]
print(imie)
imie = x[-4:18]
print(imie)


#################################
print("-" * 100)


word = "abcdfgh"

slice1 = word[:3]  # abc
slice2 = word[3:]  # dfgh

print(slice1)
print(slice2)
result = slice1 + slice2
print(result)


word = "abc def ghi"

print(word[0:7])

ile_znakow = len(word) #11
print(ile_znakow)
print(word[ile_znakow - 1]) # word[10]

ile = len("adsdsadasdwqdfewfwed")
print(ile)

#################################
print("-" * 100)

# x = input()
# y = input("Wprowadz datę: ")

print(x)
print(y)

# imie = input("Podaj swoje imię: ")
# wiek = input("Podaj swój wiek: ")
# print("Cześć " + imie + " masz " + wiek + " lat.")


# imie = input('Podaj swoje imię: ')
# wiek = input('Podaj swój wiek: ')
# print('Hej ', imie, ' masz ', wiek, ' lat.', sep="")

# klient_imie = input("Podaj Imię proszę drogi kliencie: ")
# klient_nazwisko = input("Podaj Nazwisko proszę drogi kliencie: ")
# klient_wiek = input("Podaj Wiek proszę drogi kliencie: ")

# print( "Drogi:",klient_imie, klient_nazwisko, "masz:",  klient_wiek ,"lat" )


# zmienna = input("Podaj nazwę: ")
# print(zmienna * 10)

#################################
print("-" * 100)


var = [2, 3, 4, 5, 6]
print(var)

var2 = []
var3 = [1, "ala", 3, "ma", 4.5, 'kota']
print(var3)

el0 = var3[0]
print(el0)
print(var3[0:3])

#################################
print("-" * 100)

var = [2, 3, 4, 5, 6]  #7,8
print(var)

var.append(7)
var.append(8)
print(var)


#################################
print("-" * 100)

var = [2, 3, [2, 3], 5, ["ala", "ma", "kota"]]
print(var)

# ostatni = var[-1]
# print(ostatni)

# ostatnia_l = ostatni[0]
# print(ostatnia_l)
# print(ostatnia_l[1])
var[-1][-1] = "koty"
print(var)

#################################
print("-" * 100)

liczby = [1, 2, 3]
print(liczby)

my_list = [4, 5 ,6]

# liczby.append(my_list)
print(liczby)

liczby2 = liczby[:]
liczby2.append(my_list)
print(liczby2)


#################################
print("-" * 100)


liczby = [1, 2, 3, 4, 5, 6, 7, 8, 9]

liczbyv2 = liczby[:]
print(liczbyv2)

co_drugi = liczby[1:5:2]
print(co_drugi)

#################################
print("-" * 100)

tekst = "12345"
len_t = len(tekst)
print(len_t)

idx = len_t // 2
print(idx)

print(tekst[idx])


#################################
print("-" * 100)
# zadanie 1
# * Biorąc pod uwagę ciąg o nieparzystej długości większej niż 7, zwróć łańcuch
#   złożony z trzech środkowych znaków danego ciągu:
#   * Dane wejściowe:\
#     `str1 = "Datatypes"`
#   * Oczekiwany wynik:\
#     `aty`

str1 = "Datatypes"
idx = len(str1) // 2

mid = str1[idx - 1:idx + 2]
print(mid)


# * Biorąc pod uwagę 2 ciągi, `s1` i `s2`, utwórz nowy ciąg, dodając `s2` w środku `s1`
# * Dane:
#   * `s1 = "FullStack"`
#   * `s2 = "Python”`
# * Oczekiwany wynik:\
#   `FullPythonStack`

s1 = "FullStack"
s2 = "Python"

s3 = s1[:4] + s2 + s1[4:]
print(s3)

idx = len(s1) // 2
s3 = s1[:idx] + s2 + s1[idx:]

print(s3)

print(s1[:idx], s2, s1[idx:], sep="")


#################################
print("-" * 100)



lista1 = [1, 2, 3, 4]
lista1.insert(2, "alamakota") # [1, 2, 'alamakota', 3, 4]
print(lista1)

# * Lista ma wiele użytecznych metod
#       * `.append(x)` – dodaje `x` do listy
#       * `.remove(x)` – usuwa pierwszy `x` z listy
#       * `.pop()` – usuwa i zwraca ostatni element listy
#       * `.insert(i, x)` – wstawia `x` przed indeksem `i`
#       * `.extend(x)` – dodaje na koniec listy dodatkową zmienną iterowalną `x`
#       * `.count(x)` – zwraca ilość wystąpień `x` 
#       * `.index(x)` – zwraca indeks pierwszego wystąpienia `x`
#       * `.sort()` – sortuje listę rosnąco
#   * `.reverse()` – sortuje listę w odwróconym porządku



#   * `.remove(x)` – usuwa pierwszy `x` z listy

lista1 = [1, 2, 3, 4, 1]
lista1.remove(1)   #[2, 3, 4, 1]
print(lista1)

#   * `.pop()` – usuwa i zwraca ostatni element listy

lista1 = [1, 2, 3, 4, 1]
zmienna = lista1.pop()  #[1, 2, 3, 4]
print(zmienna)
print(lista1)

# * `.extend(x)` – dodaje na koniec listy dodatkową zmienną iterowalną(lista) `x`

lista1 = [1, 2, 3, 4, 1]

lista1.extend([3, 8, 8 ,8])  # to samo co "+" [1, 2, 3, 4, 1, 3, 8, 8, 8]
print(lista1)

# * `.count(x)` – zwraca ilość wystąpień `x` 
lista1 = [1, 2, 3, 4, 1]
print(lista1.count(1))  # 2


#   * `.index(x)` – zwraca indeks pierwszego wystąpienia `x`
lista1 = [1, 2, 3, 4, 1, 8]
print(lista1.index(8))   # 5



#   * `.sort()` – sortuje listę rosnąco
lista1 = [1, 2, 3, 4, 1, 8, 0]
lista1.sort()  #[0, 1, 1, 2, 3, 4, 8]
print(lista1)


#   * `.reverse()` – odwraca kolejność
lista1 = [1, 2, 3, 4, 1, 8, 0]
lista1.reverse()  #[0, 8, 1, 4, 3, 2, 1]
print(lista1)

lista1 = [1, 2, 3, 4, 1, 8, 0]
lista1.sort()
lista1.reverse()  #[0, 8, 1, 4, 3, 2, 1]
print(lista1)

#################################
print("-" * 100)



lista1 = [1, 2, 3, 4, 1, 8, 0]
lista2 = sorted(lista1)
print(lista2)


lista1 = [1, 2, 3, 4, 1, 8, 0]
lista2 = sorted(lista1, reverse=True)
print(lista2)


