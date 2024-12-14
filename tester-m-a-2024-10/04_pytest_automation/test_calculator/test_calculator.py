from calculator import Calculator

def test_add_positive():
    """doc"""
    assert Calculator.add(3, 4) == 7

def test_subtract():
    """test to check sub method"""
    var1 = 10
    var2 = 20
    result = Calculator.subtract(var1, var2)
    assert result == -10

def test_divide_positive():
    """divide two positive vars"""
    var1 = 10
    var2 = 5
    result = Calculator.divide(var1, var2)
    assert result == 2

def test_divide_negative():
    """divide one positive, one negative vars"""
    var1 = 10
    var2 = -5
    result = Calculator.divide(var1, var2)
    assert result == -2
