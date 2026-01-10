class Calculator:
    """add, subtract, divide, multiply"""

    # def add(a, b):
    #     result = a + b
    #     return result

    # def add(a, b):
    #     if type(a) != int or type(a) != float:
    #         return None
    #     if type(b) != int or type(b) != float:
    #         return None
    #     result = a + b
    #     return result

    def add(a, b):
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            result = a + b
            return result
        else:
            return "Bad numbers not int/float"

    def subtract(num1, num2):
        """
        Subtract num2 from num1 and return result

        :param num1: Description TODO
        :param num2: Description TODO
        """
        return num1 - num2

    def divide(a, b):
        try:
            results = a / b
        except ZeroDivisionError:
            return "Zero Division Error"
        return results

    def multiply(a, b):
        return a * b
