import csv
import os

PATH = os.path.dirname(__file__) + '/items.csv'


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate: float = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.
        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        super().__init__()
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) <= 10:
            self.__name = value

        else:
            raise ValueError("Длина наименования товара превышает 10 символов")

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.
        :return: Общая стоимость товара.
        """
        calculated_price: float = self.quantity * self.price
        return calculated_price

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @classmethod
    def instantiate_from_csv(cls, filename):
        with open(filename, encoding='windows-1251') as file:
            result = csv.DictReader(file)
            for item in result:
                cls(item['name'], item['price'], item['quantity'])

    @staticmethod
    def string_to_number(value):
        result = float(value)
        result_2 = int(result)
        return result_2

    def __str__(self):
        return f'{self.name}'

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __add__(self, other):
        if isinstance(other, Item):
            return self.quantity + other.quantity
        else:
            raise TypeError('Только тип Item')
