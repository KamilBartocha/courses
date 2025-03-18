from calculator import Calculator

input_a = int(input("podaj a: "))
input_b = int(input("podaj b: "))
input_op = input("podaj znak: '+' or '-' ")

while True:
    if input_op == "+":
        result = Calculator.add(input_a, input_b)
        print(f"wynik: {result}")
        break
    elif input_op == "-":
        result = Calculator.subtract(input_a, input_b)
        print(f"wynik: {result}")
        break
    else:
        print("Not implemented yet")
        break

