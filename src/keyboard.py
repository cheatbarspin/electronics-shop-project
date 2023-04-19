from src.item import Item


class MixinLog:
    LANGUAGE = 'EN'

    def __init__(self):
        self.language = self.LANGUAGE

    def change_lang(self):
        if self.language == 'RU':
            self.language = 'EN'
        else:
            self.language = 'RU'
        return self.language


class KeyBoard(Item, MixinLog):
    pass


kb = KeyBoard('Dark Project KD87A', 9600, 5)
print(kb.language)
kb.change_lang()

print(kb.language)