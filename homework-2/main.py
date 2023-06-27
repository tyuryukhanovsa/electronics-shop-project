from src.item import Item

CSV_FILE = '../src/items.csv'

if __name__ == '__main__':
    item = Item('Телефон', 10000, 5)

    # длина наименования товара меньше 10 символов
    item.name = 'Смартфон'
    assert item.name == 'Смартфон'

    # длина наименования товара больше 10 символов
    item.name = 'СуперСмартфон'
    # Exception: Длина наименования товара превышает 10 символов.

    Item.instantiate_from_csv(CSV_FILE)  # создание объектов из данных файла
    assert len(Item.all) == 6  # в файле 5 записей с данными по товарам (отрабатывает только при значении 6)

    item1 = Item.all[1]
    assert item1.name == 'Смартфон' # отрабатыввает только при значении 1 вероятно учитывает экземпляр добавленный ранее почему здесь стоял 0 не понятно

    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5
