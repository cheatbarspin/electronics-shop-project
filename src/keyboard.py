from src.item import Item


class MixinLog:
    LANGUAGE = 'EN'

    def __init__(self):
        self.__language = self.LANGUAGE

    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, value):
        if value == 'EN' or value == 'RU':
            self.__language = value
        else:
            raise AttributeError('property error : такая раскладка не задана')

    def change_lang(self):
        if self.__language == 'RU':
            self.__language = 'EN'
        else:
            self.__language = 'RU'
        return self


class KeyBoard(Item, MixinLog):
    def __str__(self):
        return f'{self.name}'


# kb = KeyBoard('Dark Project KD87A', 9600, 5)
# print(kb.language)
# kb.change_lang().change_lang()
# print(kb.language)
# kb.language = 'DE'

