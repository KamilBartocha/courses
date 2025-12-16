punkty = 70

if punkty >= 90:
    print("zdałeś na 5!")
elif punkty >=80 and punkty < 90:
    print("Zdałeś na 4")
elif punkty >=70:
    print("Zdałeś na 3")
elif punkty >=60:
    print("Zdałeś na 2")
else:
    print("Nie zdałeś :(")

print("poza ifem")



x = "Zdałeś" if punkty >= 50 else None
print(x)



print("*" * 120)

list1 = [1, 2, 3, 4, 5]
for number in list1:
    print(number * 100)

for number in list1:
    print("hello world")

for number in range(2, 7, 2): #(start, stop, step)
    print("hello2", number)



warzywa = ('marchew', 'kalafior', 'kapusta')

for w in warzywa:
    print('warzywo:', w)