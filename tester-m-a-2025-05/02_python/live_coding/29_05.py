# 25.05.2025

# x = 20
# y = 3.14
# z = "tekst do wyświetlenia"

# x + y
# x - y
# x / y
# x * y
# x ** y
# x // y
# x % y

# print(x)

x = "ala ma kota "
x = 'ala ma kota '

y = "A"
z = ""


text = "Hello  x "

print("-" * 100)

print("ćw 1")

print("-" * 100)

print("\t\tala ma kota\nnowa linia")




"""

    to jest kod
        który



        liczy liczbę pi


  ####
    print()


"""

# wyświetl F

text = "ala ma kota Filemona"

print(text[12]) #dodatni

print(text[-8]) #ujemny


litera_imie_kota = text[-8]

print(litera_imie_kota)




text = "ala ma koty Filemona i Boba"


imie_kota = text[12] + text[13] + text[14] + text[15] + text[16] + text[17] + text[18] + text[19]
print(imie_kota)

imie_kota2 = text[12:20]
print(imie_kota2)


# wypisz jeden z miesięcy - dowolnie wybrany
text = 'Maj Czerwiec Lipiec Sierpień'

print(text[:3])
print(text[0:3])
print(text[-8:])
print(text[4:12])
print(text[20:])
print(text[13:19])

i1 = text.find("Czerwiec")
i2 = text.find(" Lip")
print(text[i1:i2])




# print()
# len()


text = "Ala ma kota"
l = len(text)

print(l)
print(text[l - 1])   # l - 1 => 10 => text[10]



print("*" * 100)


# lata = input()
# oprocentowanie = input("Wprowadź oprocentowanie: ")

# print(lata)
# print(oprocentowanie)

# imie = input('Jak masz na imię? ')
# wiek = input('Ile masz lat? ')
# print('Jesteś ' + imie + " masz " + wiek + " lat")


# imie = input('Podaj swoje imie: ')
# wiek = input('Podaj swój wiek: ')
# print("Twoje imię to " + imie)
# print('Masz ' + wiek + ' lat')



imiona = ["Ala", "Bob", "Mark", "Ashwin", "Manisha"]
#           0       1    2        3          4
print(imiona)

print(imiona[0])

print(imiona[0:2])


temp = [21, 22, 15, 10, 30, 21, 12, 15]

print(temp[-1])




lista1 = [1, 2, 3, 4]

lista2 = [6, 7, 8, 9]

lista_suma = lista1 + lista2 + lista1 + lista1
print(lista_suma)




lista_x = [1, 2, 4, 4]

lista_x[2] = "ala"

print(lista_x)


lista_x.append(5)
print(lista_x)


x = [1, 2, ["ala" , "ma", "kota"]]

print(x[0])
print(x[2])









x = "Python jest git"

# x[start:stop] start - włącznie, stop - wyłącznie
# x[1:3]  1, 2

print(x[1:3])   # x[1] + x[2]  3-nie
#               wynik:  yt




lista_imion = ["imie1", "imie2"]

print(lista_imion)     #['imie1', 'imie2']
print(lista_imion[0])  #imie1

lista_imion.append("Ala") #['imie1', 'imie2', 'Ala']
print(lista_imion)        #['imie1', 'imie2', 'Ala']



print("\n\n\n\n\n\n\n\n")
num = 10
print(num)
print(type(num))


num2 = 2.7
print(num2)
print(type(num2))


#konwersje

# int(x)    # zmienia x na int
# float(y)  # zmienia y na float
# str(z)    # zmienia z na str

# # x = "33"
# # x_i = int(x)   teraz x_i jest int

# type() #możemy wyświetlić

print("\n\n\n\n\n\n\n")
x = "22"
x_int = int(x)
print(type(x_int))

print(x_int + 10)



print("\n\n\n\n\n\n\n")

