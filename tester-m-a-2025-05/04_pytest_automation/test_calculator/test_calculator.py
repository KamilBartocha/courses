from calculator import Calculator

def test_add_two_positive():
    expected = 10
    result = Calculator.add(6, 4)
    assert result == expected

def test_add_two_negative():
    expected = -10
    result = Calculator.add(-6, -4)
    assert result == expected

def test_add_positive_zero():
    result = Calculator.add(20, 0)
    expected = 20
    assert result == expected

def test_subtract_two_positive():
    result = Calculator.subtract(20, 10)
    expected = 10
    assert result == expected

def test_subtract_two_negative():
    result = Calculator.subtract(-20, -10)
    expected = -10
    assert result == expected

def test_divide_positive():
    """EKSTRA, najlepiej wyjątiem"""
    result = Calculator.divide(20, 10)
    expected = 2
    assert result == expected

def test_divide_by_zero():
    """EKSTRA, najlepiej wyjątiem"""
    result = Calculator.divide(20, 0)
    expected = "Undefined"
    assert result == expected

