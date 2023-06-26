from src.item import Item
import pytest


@pytest.fixture
def test_data():
    return Item("Смартфон", 30000, 10)


def test_calculate_total_price(test_data):
    assert test_data.calculate_total_price() == 300000


def test_apply_discount(test_data):
    Item.pay_rate = 0.7
    test_data.apply_discount()
    assert test_data.price == 21000
