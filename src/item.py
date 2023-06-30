import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

    def __repr__(self):
        return f'{self.__class__.__name__}{self.__name, self.price, self.quantity}'

    def __str__(self):
        return str(self.__name)

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        total_price = self.price * self.quantity
        return total_price

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= Item.pay_rate

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if len(new_name) > 10:
            self.__name = new_name[:10]
        else:
            self.__name = new_name

    @classmethod
    def instantiate_from_csv(cls, csv_file):
        """класс-метод, инициализирующий экземпляры класса
           Item данными из файла *.csv
        """
        with open(csv_file, 'r', encoding='windows-1251') as file:
            file_reader = csv.DictReader(file, delimiter=",")
            for row in file_reader:
                name = str(row["name"])
                price = float(row["price"])
                quantity = int(row["quantity"])
                cls(name, price, quantity)

    @staticmethod
    def string_to_number(num_in_str: str):
        """
        Метод возвращающий число из числа-строки
        """
        return int(float(num_in_str))
