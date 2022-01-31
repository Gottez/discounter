import discount
import pytest
from pytest import approx


#Test Member
def test_member1():
    result = discount.calculate_discount(1, True)
    assert result == approx(1/5)

def test_member2():
    result = discount.calculate_discount(3, True)
    assert result == approx(2/5)

def test_member3():
    result = discount.calculate_discount(4, True)
    assert result == approx(58/125,rel=1e-2)

def test_member4():
    result = discount.calculate_discount(6, True)
    assert result == approx(3/5,rel=1e-2)

#Test no Member
def test_nomember1():
    result = discount.calculate_discount(1, False)
    assert result == (0)

def test_nomember2():
    result = discount.calculate_discount(3, False)
    assert result == (1/4)

def test_nomember3():
    result = discount.calculate_discount(4, False)
    assert result == approx(1/3)

def test_nomember4():
    result = discount.calculate_discount(6, False)
    assert result == (1/2)


def test_expect_error1():
    with pytest.raises(ValueError) as error_info:
        calculate_discount(0, False)
    assert str(error_info.value) == "amount has to be greater than 0 and less or equal to 10"
    assert error_info.type == ValueError

def test_expect_error2():
    with pytest.raises(ValueError) as error_info:
        calculate_discount(11, False)
    assert str(error_info.value) == "amount has to be greater than 0 and less or equal to 10"
    assert error_info.type == ValueError

def test_expect_error3():
    with pytest.raises(ValueError) as error_info:
        calculate_discount(0, True)
    assert str(error_info.value) == "amount has to be greater than 0 and less or equal to 10"
    assert error_info.type == ValueError

def test_expect_error4():
    with pytest.raises(ValueError) as error_info:
        calculate_discount(11, True)
    assert str(error_info.value) == "amount has to be greater than 0 and less or equal to 10"
    assert error_info.type == ValueError


def test_expect_error5():
    with pytest.raises(ValueError) as error_info:
        calculate_discount("A", True)
    assert str(error_info.value) == "amount must be an int"
    assert error_info.type == ValueError

def test_expect_error6():
    with pytest.raises(ValueError) as error_info:
        calculate_discount("A", False)
    assert str(error_info.value) == "amount must be an int"
    assert error_info.type == ValueError
