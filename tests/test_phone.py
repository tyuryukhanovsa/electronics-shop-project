from src.item import Item
from src.phone import Phone
from src.item import Item
import pytest


def test_number_of_sim():
    phone1 = Phone("iPhone 14", 120_000, 10, 1)
    assert phone1.number_of_sim == 1


if __name__ == '__main__':
    phone2 = Phone("iPhone 14", 120_000, 10, 1)
    item1 = Item("Смартфон", 10000, 20)
    assert item1 + phone2 == 30
    assert str(phone2) == 'iPhone 14'
