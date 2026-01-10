from calculator import Calculator


def test_add_two_positive():
    expected = 10
    result = Calculator.add(6, 4)
    assert result == expected

def test_add_positive_and_str():
    expected = "Bad numbers not int/float"
    result = Calculator.add(6, "4")
    assert result == expected

def test_subtract_two_positive():
    expected = 11
    result = Calculator.subtract(20, 9)
    assert result == expected  # 11 == 11


def test_add_two_negavtives():
    expected = -10
    result = Calculator.add(-6, -4)
    assert result == expected


def test_substract_two_positives():
    expected = 2
    result = Calculator.subtract(6, 4)
    assert result == expected


def test_substract_two_negatives():
    expected = -2
    result = Calculator.subtract(-6, -4)
    assert result == expected


def test_divide_two_positives():
    expected = 2
    result = Calculator.divide(8, 4)
    assert result == expected


def test_divide_two_negatives():
    expected = 2
    result = Calculator.divide(-8, -4)
    assert result == expected


def test_multiply_two_positives():
    expected = 4
    result = Calculator.multiply(2, 2)
    assert result == expected


def test_multiply_two_negatives():
    expected = 4
    result = Calculator.multiply(-2, -2)
    assert result == expected

def test_divide_by_zero():
    expected = "Zero Division Error"
    result = Calculator.divide(-8,0)
    assert result == expected