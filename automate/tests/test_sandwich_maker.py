from scripts.sandwichMaker import (
    choose_bread
)
from pytest import raises

def test_choose_bread():
    assert choose_bread('wheat') == 2.5
    assert choose_bread('white') == 2
    assert choose_bread('sourdough') == 2.75
    with raises(Exception):
        choose_bread('asdf')