class Calculator:
    # def add(a, b):
    #     try:
    #         result = a + b
    #         return result
    #     except TypeError:
    #         return "cant add number and letter"
    # def add(a, b):
    #     if type(a) == str or type(b) == str:
    #         return "cant add number and letter"
    #     else:
    #         return a + b

    def add(a, b):
        if isinstance(a, str) or isinstance(b, str):
            return "cant add number and letter"
        else:
            return a + b

    def subtract(a, b):
        """ Calculate a - b """
        return a - b

    def multiply(a, b):
        return a * b

    # def divide(a, b):
    #     if b == 0:
    #         return "Zero division error!"
    #     result = a / b
    #     return result

    def divide(a, b):
        try:
            result = a / b
            return result
        except ZeroDivisionError:
            return "Zero division error!"
