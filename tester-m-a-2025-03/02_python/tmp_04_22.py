## Functions

# len()
# print()
# sorted()

def print_hello():
    print("hello")
    print("koniec_funkcji")


print_hello()
print("po prostu")
print_hello()


def create_upper_str(var):
    ''' Checks if var(argument) is str type.
        if it is str, then all chars are transformed into upper case
        if not, str="nie można zwiększyć, nie podałes str jako argumentu"
        is returned
    '''
    if type(var) == str:
        result = var.upper()
    else:
        result = "nie można zwiększyć, nie podałes str jako argumentu"
    return result

x = create_upper_str("alama_kota")
print(x)

y = create_upper_str(6)
print(y)

def create_upper_str_2(var):
    if type(var) == str:
        result = var.upper()
    else:
        result = "nie można zwiększyć, nie podałes str jako argumentu"
    print(result)

create_upper_str_2("alama_kota")

create_upper_str_2(6)




def add_3_numbers(ala, ma, kota):
    if type(ala) == type(ma) == type(kota):
        wynik = ala + ma + kota
    else:
        wynik = "nie można dodać!"
    return wynik

x = add_3_numbers("a", "b", "c")
y = add_3_numbers(5, 2, 1)

print(x)
print(y)


def add_3_numbers2(ala, ma, kota):
    if isinstance(ala, (int, float)) and isinstance(ma, (int, float)) and isinstance(kota, (float, int)):
        wynik = ala + ma + kota
    else:
        wynik = "nie można dodać!"
    return wynik

x = add_3_numbers2("a", "b", "c")
y = add_3_numbers2(5, 2, 1)

print(x)
print(y)

y = create_upper_str




def suma_for(number):
    """counts sum form 1 to number.
    if number = 3 returns 1 + 2 + 3"""
    suma = 0
    for i in range(number + 1):
        suma = suma + i
        print(f"zmienna i: {i} Suma: {suma}")
    return suma

suma_for(3)


def suma_rekurencja(number):
    if number == 0:
        return 0
    else:
        print(f"Zmienna number: {number}")
        return number + suma_rekurencja(number - 1)


print(f"Suma za pomocą rekurencji: {suma_rekurencja(3)}")





### wyjątki


print("alamakota1")


lista = [1, 2, 3]

try:
    x = lista[0] + lista[5]
except Exception:
    print("coś poszło nie tak z dodaniem wartości, czy lista ma 6 elemntów?")






print("alamakota2")









def test_1():
    print(j)
    print("alamakota_1")

def test_2():
    print("alamakota_2")
    print(1/0)

def test_3():
    print("alamakota_3")


try:
    test_1()
except Exception as er:
    print("coś poszło nie tak, test się wywalił :(((")
    print(er)

try:
    test_2()
except Exception as errr:
    print("coś poszło nie tak, test się wywalił :(((")
    print(errr)

try:
    test_3()
except Exception as blad:
    print("coś poszło nie tak, test się wywalił :(((")
    print(blad)




print("*" * 80)



print("1")

rest_api_response = [None]


if len(rest_api_response) == 0:
    raise Exception("restAPI zwróciło pustą listę!!!")


print(rest_api_response[0])


inpt = input("podaj rok urodzenia: ")

try:
    inpt = int(inpt)
except ValueError:
    print("Chyba nie podałeś liczby??")
else:
    print(2025 - inpt)
finally:
    print("Koniec")






### Ćwiczenie nr 1:
# Napisz program, który poprosi użytkownika o podanie dwóch liczb.

# * Dodaj wprowadzone liczny i wypisz wynik.
# * Jeśli nie zostanie wprowadzona liczba, zwróć komunikat o błędzie i poproś ponownie.
# * dodaj obsługę wyjątku w przypadku błędu konwersji znaku na liczbę



num1 = input("podaj 1 liczbę: ")
num2 = input("podaj 2 liczbę: ")

while True:
    try:
        num1 = int(num1)
        num2 = int(num2)
    except Exception:
        print("na pewno podałes liczby?")
    else:
        result = num1 + num2
        print(result)
        break
