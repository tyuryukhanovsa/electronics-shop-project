from src.item import Item
import pytest


@pytest.fixture
def test_data():
    return Item("Смартфон", 30000, 10)


def test_calculate_total_price(test_data):
    assert test_data.calculate_total_price() == 300000
