from calculator import Calculator

def test_add_two_positive():
    expected = 10
    result = Calculator.add(6, 4)
    assert result == expected

def test_add_two_negative():
    expected = -10
    result = Calculator.add(-6, -4)
    assert result == expected

def test_add_number_and_letter():
    expected = "cant add number and letter"
    result = Calculator.add(3, "a")
    assert expected == result

def test_add_number_and_letter_2():
    expected = "cant add number and letter"
    result = Calculator.add("a", 3)
    assert expected == result

def test_subtract_two_positive():
    expected = 12
    result = Calculator.subtract(30, 18)
    assert expected == result

def test_subtract_two_negative():
    expected = -12   # -30 -(-18) => -12
    result = Calculator.subtract(-30, -18)
    assert expected == result

def test_multiply_positive():
    expected = 8
    result = Calculator.multiply(2, 4)
    assert expected == result

def test_multiply_negative():
    expected = 8
    result = Calculator.multiply(-2, -4)
    assert expected == result

def test_divide_positive():
    expected = 2
    result = Calculator.divide(4, 2)
    assert expected == result

def test_divide_negative():
    expected = 2
    result = Calculator.divide(-4, -2)
    assert expected == result

def test_divide_zero():
    expected = "Zero division error!"
    result = Calculator.divide(4, 0)
    assert expected == result