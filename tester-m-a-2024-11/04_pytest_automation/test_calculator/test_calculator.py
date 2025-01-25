from calculator import Calculator

def test_cal_add_two_positive_v1():
    result = Calculator.add(3, 10)
    if result == 13:
        print("pass")
    else:
        raise AssertionError(f"FAIL result:{result}!=13")

def test_cal_add_two_positive_2():
    result = Calculator.add(3, 10)
    assert type(result) == int
    assert result == 13

def test_cal_add_two_negative():
    result = Calculator.add(-3, -1011)
    assert type(result) == int
    assert result == -1014

def test_cal_add_one_pos_one_negative():
    result = Calculator.add(100, -1211)
    assert type(result) == int
    assert result == -1111

def test_cal_add_two_zeros():
    result = Calculator.add(0, 0)
    assert type(result) == int
    assert result == 0

def test_cal_subtract_two_positive():
    result = Calculator.subtract(10, 20)
    assert isinstance(result, int)
    assert result == -10