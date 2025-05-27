# # 3 z pliku 003

# s1 = "America"
# s2 = "Japan"

# pierwsze_l = s1[0] + s2[0]  # AJ

# mid_s1 = len(s1) // 2
# mid_s2 = len(s2) // 2

# srodkowe_l = s1[mid_s1] + s2[mid_s2]  # s1[3] + s2[2] => r + p

# ostatnie_l = s1[-1] + s2[-1]   # a + n

# result = pierwsze_l + srodkowe_l + ostatnie_l

# print(result)  # AJrpan

# # roz 2
# print(s1[0] + s2[0] + s1[len(s1) // 2] + s2[len(s2) // 2] + s1[-1] + s2[-1])


# #roz 3

# AMs1 = "America"
# JAs1 = "Japan"
# AMJAresult = AMs1[0]+JAs1[0]+AMs1[len(AMs1)//2]+JAs1[len(JAs1)//2]+AMs1[-1]+JAs1[-1]
# print(AMJAresult)

# # roz3

# s1 = "America"
# s2 = "Japan"
# indeksik_a = len(s1) // 2
# indeksik_j = len(s2) // 2
# s3 = s1[0] + s2[0] + s1[indeksik_a] + s2[indeksik_j] + s1[-1] + s2[-1]
# print(s3)

# #################################
# print("-" * 100)


# # zad 4

# str1 = "Python"

# str2 = str1[::-1]

# print(str2)

# # inny sposób
# str1_rev1 = ''.join(reversed(str1))
# print(str1_rev1)


# # zad 5

# print("Ćwiczenie 5:")
# lista1 = ["Przemysław", "Michał", "Tomasz", "Yelyzaveta", "Piotr", "Jakub", "Maciej", "Maciej", "Jacek", "Aleksandra", "Agnieszka", "Dorota"]
# lista2 = sorted(lista1)
# lista1.sort()
# ile_elementow = len(lista2)
# # print(lista1)
# # print(lista2)
# print("Lista:", lista1)
# print("Ma ona długość", ile_elementow)

# # roz 2

# kursanci_list = ["MichalG", "MaciejP", "MaciejS"]
# print(kursanci_list)
# kursanci_list.sort()
# kursanci_list_rev = sorted(kursanci_list, reverse=False)
# print(kursanci_list)
# print(kursanci_list_rev)
# ilosc_kursantow=len(kursanci_list)
# print(ilosc_kursantow)





# x = 1
# y = 1.3
# z = int(y)
# r = str(x)

# print(r + "ala")

# lista1 = [5, 1, 4]

# list2 = sorted(lista1)

# #################################
# print("-" * 100)


# x = {1: "ala", 2: "ma", 3: "kota", "3": 32}
# y = {"TR3234242": "ala", "TR234234243": "ma", "TR3242343244": "psa"}

# print(x)
# print(y)

# print(type(x))

# print(x[1])
# print(y["TR3234242"])

# x[7] = "filemon"
# print(x)

# y["TR32424"] = "rudolf"
# print(y)

# z = {"TR3234242": "ala", "TR234234243": "ma", "TR3242343244": ["psa", "filemona"], 1:2}
# print(z)


# #################################
# print("-" * 100)


# y2 = {"TR3234242": "ala", "TR234234243": "ma", "TR3242343244": "psa"}

# print(y2)

# keys = y2.keys()
# print(keys)

# values = y2.values()
# print(values)

# items = y2.items()
# print(items)




# lista2 = [2 ,1 ,2 ,3, 5 ,3, 1]

# x = set(lista2)
# print(x)
# x.update([2, 4])

# y = list(x)
# print(y)


#################################
print("-" * 100)

temperatura = 40

if temperatura > 23:
    print("jest")
    print("ciepło")
elif temperatura > 10:
    print("jest neutralnie")
else:
    print("jest")
    print("zimno")
print("poza wcięciem")


if temperatura > 0:
    print("alamakota")


print("jest ciepło") if temperatura > 23 else print("jest zimno")


#################################
print("-" * 100)


lista1 = [1, 0, 3, 4, 5]

for el in lista1:
    print("Element")
    print(el)
    print(f"element * 2: {el * 2}")
    print("koniec pętli")

print("po pętli")

#################################
print("-" * 100)

for el in range(5):
    print("hello world")

for _ in range(10):
    print("hello")

#################################
print("-" * 100)

lista1 = [1, 0, 3, 4, "ala", 2, "ma"]

list_int = []
list_str = []
for el in lista1:
    if type(el) == int:
        list_int.append(el)
    elif type(el) == str:
        list_str.append(el)

print(list_int)
print(list_str)

