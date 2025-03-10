from calculator import Calculator

input_a = input("podaj a: ")
input_b = input("podaj b: ")
input_op = input("podaj znak: + or - ")

while True:
    if input_op == "+":
        result = Calculator.add(input_a, input_b)
        print(result)
    else:
        print("Not implemented yet")
