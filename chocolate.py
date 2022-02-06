from datetime import date
from decimal import Decimal
import pytest

def calculate_price(total: Decimal, day: date) -> Decimal:

    print(total)
    print(day)

#calculate_price(Decimal("10.1"), date(2020, 12, 24))


price_test_data = [

#rabatt = 5% - vEP1-1 : [0, …, 50]
pytest.param(Decimal("0"), date(2022, 4, 12), Decimal("0"), id="vEp1.1.1"),

#nächste zeile liefert gleiches ergebnis wie ohne rabatt!
pytest.param(Decimal("0.01"), date(2022, 4, 12), Decimal("0.01"), id="vEp1.1.2"),

pytest.param(Decimal("0.11"), date(2022, 4, 12), Decimal("0.1"), id="vEp1.1.3"),

pytest.param(Decimal("42"), date(2022, 4, 12), Decimal("39.9"), id="vEp1.1.4"),

pytest.param(Decimal("50"), date(2022, 4, 12), Decimal("47.5"), id="vEp1.1.5"),

#rabatt = 10 % - vEP1-2 : ]50, …, 100]
pytest.param(Decimal("50.01"), date(2022, 4, 12), Decimal("45.01"), id="vEp1.2.1"),

pytest.param(Decimal("50.02"), date(2022, 4, 12), Decimal("45.02"), id="vEp1.2.2"),

pytest.param(Decimal("79"), date(2022, 4, 12), Decimal("71.1"), id="vEp1.2.3"),

pytest.param(Decimal("100"), date(2022, 4, 12), Decimal("90"), id="vEp1.2.4"),

#rabatt = 15 % - vEP1-3 : ]100, …, max_decimal]
pytest.param(Decimal("100.01"), date(2022, 4, 12), Decimal("85.01"), id="vEp1.3.1"),

pytest.param(Decimal("100.02"), date(2022, 4, 12), Decimal("85.02"), id="vEp1.3.2"),

pytest.param(Decimal("1337"), date(2022, 4, 12), Decimal("1136.45"), id="vEp1.3.3"),

#rabatt = 0% - vEP2-1 : [min_date, …, (2022, 4, 8)]
pytest.param(Decimal("79"), date(2022, 4, 5), Decimal("79"), id="vEp2.1.1"),

pytest.param(Decimal("79"), date(2022, 4, 8), Decimal("79"), id="vEp2.1.2"),

#rabatt = 15% - vEP2-1 : [min_date, …, (2022, 4, 8)]
pytest.param(Decimal("79"), date(2022, 4, 9), Decimal("71.1"), id="vEp2.2.1"),

pytest.param(Decimal("79"), date(2022, 4, 10), Decimal("71.1"), id="vEp2.2.2"),

pytest.param(Decimal("79"), date(2022, 4, 12), Decimal("71.1"), id="vEp2.2.3"),

pytest.param(Decimal("79"), date(2022, 4, 17), Decimal("71.1"), id="vEp2.2.4"),

pytest.param(Decimal("79"), date(2022, 4, 18), Decimal("71.1"), id="vEp2.2.5"),

#rabatt = 0% vEP2-3 : [(2022, 4, 19), …, max_date]
pytest.param(Decimal("79"), date(2022, 4, 19), Decimal("79"), id="vEp2.3.1"),

pytest.param(Decimal("79"), date(2022, 4, 27), Decimal("79"), id="vEp2.3.2")]

@pytest.mark.parametrize("total,day,expected_price", price_test_data)
def test_valid_price(total, day, expected_price):
    price = calculate_price(total, day)
    assert price == expected_price


def test_error1():
    with pytest.raises(ValueError) as error_info:
        calculate_price("test", date(2022, 4, 12))
    assert str(error_info.value) == "amount must be a decimal value"
    assert error_info.type == ValueError

def test_error2():
    with pytest.raises(ValueError) as error_info:
        calculate_price(10.001, date(2022, 4, 12))
    assert str(error_info.value) == "amount must be a two digit decimal value"
    assert error_info.type == ValueError

def test_error3():
    with pytest.raises(ValueError) as error_info:
        calculate_price(10, date(2022, 4, 12))
    assert str(error_info.value) == "amount must be a two digit decimal value"
    assert error_info.type == ValueError
    
def test_error4():
    with pytest.raises(ValueError) as error_info:
        calculate_price(Decimal("10.1"), "test")
    assert str(error_info.value) == "date is not valid"
    assert error_info.type == ValueError
    
def test_error5():
    with pytest.raises(ValueError) as error_info:
        calculate_price(Decimal("10.1"), "")
    assert str(error_info.value) == "date is not valid"
    assert error_info.type == ValueError

def test_error6():
    with pytest.raises(ValueError) as error_info:
        calculate_price("", date(2022, 4, 12))
    assert str(error_info.value) == "amount must be a two digit decimal value"
    assert error_info.type == ValueError
