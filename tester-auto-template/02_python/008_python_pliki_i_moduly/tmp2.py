# try:
#     f = open("x.txt", 'r')
# except Exception as er:
#     print(f"Nie udało się! {type(er)} Błąd: {er}")

# import os
# print(os.listdir())
# print(os.listdir('/Users/kamil/Repositories/courses/tester-m-a-2024/python'))


# 'r' -> read(), readline()


# file = open('008_file_text.txt', 'r')

# x = file.readline()
# y = file.readline()
# print(x)
# print("2:", y)


# file.close()

# file = open('008_file_text.txt', 'r')

# x = file.readlines()
# print(x)
# print(x[0])  #'Co to jest język Python?\n'


# file.close()


# file = open('008_file_text.txt', 'r')

# for line in file:
#     print(line)

# file.close()

# new_file = open('2.txt', 'w')

# new_file.write("Ala ma kotaaaaaa")


# new_file.close()



# new_file = open('2.txt', 'a')
# new_file.write("Ala ma kota2\n")
# new_file.close()


# read = open('2.txt')
# print(read.read())
# read.close()

# new_file = open('2.txt', 'a')
# new_file.write("Ala ma kota2\n")
# x = x + '3'
# new_file.close()


# with open('008_file_text.txt', 'r') as new:
#     print(new.read())


with open('008_file_text2.txt', 'w') as new:
    # x = x + '3'
    ile_znakow = new.write("alaas21323132dadda")
    print(ile_znakow)


# import math
# x = sqrt(9)