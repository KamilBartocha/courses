class Calculator:
    def add(a, b):
        return a + b

    def subtract(a, b):
        """subtract a - b"""
        return a - b

    def divide(a, b):
        try:
            result = a / b
            return result
        except ZeroDivisionError:
            return "Undefined"