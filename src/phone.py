from src.item import Item


class Phone(Item):

    def __init__(self, name, price, quantity, number_of_sim):
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, value):
        if value > 0:
            self.__number_of_sim = value
        else:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"


class IphoneCharger(Phone):

    def __init__(self, name, price, quantity, number_of_sim=None):
        super().__init__(name, price, quantity, number_of_sim)

    def __add__(self, other):
        if type(other) in (IphoneCharger, Phone):
            return self.quantity + other.quantity
        else:
            raise TypeError('Только зарядки для IPhone можно сложить с классом Phone')
#
#
# item1 = Item('Смартфон', 10000, 10)
# phone1 = Phone('Iphone', 10_000, 3, 1)
# ch1 = IphoneCharger('Lightning', 500, 130)
# # print(item1 + phone1)
# print(item1 + ch1)

