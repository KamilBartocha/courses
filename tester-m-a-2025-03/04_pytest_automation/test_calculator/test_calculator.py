from calculator import Calculator

def test_add_two_positive():
    expected = 10
    result = Calculator.add(6, 4)
    assert result == expected

def test_add_two_negative():
    expected = -10
    result = Calculator.add(-6, -4)
    assert result == expected

def test_add_zero_to_positive():
    """ Add positive number and 0.
    expect correct result"""
    expected = 44
    result = Calculator.add(0, 44)
    assert result == expected

def test_subtract_two_positive():
    expected = 11
    result = Calculator.subtract(20, 9)
    assert expected == result