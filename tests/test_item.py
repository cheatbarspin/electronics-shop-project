"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item, PATH


@pytest.fixture
def item1():
    return Item("Смартфон", 10000, 20)


def test_item_init(item1):
    assert item1.name == "Смартфон"
    assert item1.price == 10000
    assert item1.quantity == 20


def test_calculated_total_price(item1):
    assert item1.calculate_total_price() == 200000


def test_property(item1):
    item1.name = "Ноут"
    assert item1.name == 'Ноут'
    with pytest.raises(ValueError):
        item1.name = 'Салями с Пиццой'


def test_staticmethod():
    assert Item.string_to_number("6.0") == 6


def test_classmethod():
    Item.all.clear()
    Item.instantiate_from_csv(PATH)
    assert len(Item.all) == 5


def test_repr(item1):
    assert repr(item1) == "Item('Смартфон', 10000, 20)"
    assert str(item1) == 'Смартфон'