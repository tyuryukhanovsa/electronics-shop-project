from src.item import Item
import pytest

from src.phone import Phone


@pytest.fixture
def csv_file():
    return '../src/items.csv'


@pytest.fixture
def test_data():
    return Item("Смартфон", 30000, 10)


def test_calculate_total_price(test_data):
    assert test_data.calculate_total_price() == 300000


def test_apply_discount(test_data):
    Item.pay_rate = 0.7
    test_data.apply_discount()
    assert test_data.price == 21000


def test_name(test_data):
    test_data.name = 'Смартфон'
    assert test_data.name == 'Смартфон'

    # длина наименования товара больше 10 символов
    test_data.name = 'СуперCмартфон'
    assert test_data.name == 'СуперCмарт'


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_instantiate_from_csv(csv_file):
    Item.all = []
    Item.instantiate_from_csv(csv_file)  # создание объектов из данных файла
    assert len(Item.all) == 5


def test_repr_and_str(test_data):
    assert repr(test_data) == "Item('Смартфон', 30000, 10)"
    assert str(test_data) == 'Смартфон'


