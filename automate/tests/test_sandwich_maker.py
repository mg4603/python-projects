from scripts.sandwichMaker import (
    choose_bread,
    choose_protein
)
from pytest import raises

def test_choose_bread():
    assert choose_bread('wheat') == 2.5
    assert choose_bread('white') == 2
    assert choose_bread('sourdough') == 2.75
    with raises(Exception):
        choose_bread('asdf')

def test_choose_protein():
    assert choose_protein('chicken') == 2
    assert choose_protein('turkey') == 2.35
    assert choose_protein('ham') == 2.5
    assert choose_protein('tofu') == 3.5
    with raises(Exception):
        choose_protein('asf')