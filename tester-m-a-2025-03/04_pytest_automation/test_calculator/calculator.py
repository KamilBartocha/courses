class Calculator:
    def add(a, b):
        return a + b

    def subtract(a, b):
        """Subtract b from a and return result"""
        return  a - b

    def divide(a, b):
        """Divide a / b """
        try:
            res = a / b
        except ZeroDivisionError:
            res = "nie wolno dzielić przez 0!"
        return res

    def multiply(a, b):
        return a * b
