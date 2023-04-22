import pytest
from src.keyboard import KeyBoard


@pytest.fixture
def keyboard1():
    return KeyBoard('Dark Project KD87A', 9600, 5)


def test_keyboard_str(keyboard1):
    assert str(keyboard1) == "Dark Project KD87A"
    assert str(keyboard1.language) == "EN"


def test_change_language(keyboard1):
    keyboard1.change_lang()
    assert keyboard1.language == 'RU'
    keyboard1.change_lang()
    assert keyboard1.language == 'EN'
    with pytest.raises(AttributeError):
        raise AttributeError('такая раскладка не задана')



