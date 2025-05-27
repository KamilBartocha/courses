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

def test_divide_two_positive():
    num1 = 10
    num2 = 2
    result = Calculator.divide(num1, num2)
    assert result == 5

def test_divide_two_negative():
    num1 = -10
    num2 = -2
    result = Calculator.divide(num1, num2)
    assert result == 5

def test_divide_two_mixed():
    num1 = -10
    num2 = 2
    result = Calculator.divide(num1, num2)
    assert result == -5

def test_divide_two_mixed():
    num1 = -10
    num2 = 0
    result = Calculator.divide(num1, num2)
    assert result == "nie wolno dzielić przez 0!"

def test_multiply_two_positive():
    num1 = 10
    num2 = 20
    res = Calculator.multiply(num1, num2)
    assert res == 200
