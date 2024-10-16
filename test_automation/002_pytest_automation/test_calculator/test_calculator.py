from calculator import Calculator

def test_add_positive():
    """doc"""
    assert Calculator.add(3, 4) == 7

def test_add_negative():
    '''doc TODO'''
    result = Calculator.add(-10, -11)
    assert result == -21

def test_add_two_zeros():
    '''doc TODO'''
    result = Calculator.add(0, 0)
    assert result == 0

def test_subtract_positive_numbers():
    '''doc TODO'''
    result = Calculator.subtract(10, 8)
    assert result == 2


