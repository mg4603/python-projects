from scripts.sandwichMaker import (
    choose_bread,
    choose_cheese,
    choose_protein,
    sandwich_cost
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

def test_choose_cheese():
    assert choose_cheese('cheddar') ==  1
    assert choose_cheese('swiss') == 1.5
    assert choose_cheese('mozzarella') == 1.05
    with raises(Exception):
        choose_cheese('asdf')

def test_sandwich_cost():
    assert sandwich_cost('wheat', 'chicken', 'yes', 'cheddar', 'yes', 'yes', 'yes', 'yes') == 8.5
    assert sandwich_cost('wheat', 'chicken', 'no', 'cheddar', 'yes', 'yes', 'yes', 'yes') == 7.5
    assert sandwich_cost('wheat', 'chicken', 'no', '', 'yes', 'yes', 'yes', 'yes') == 7.5
    assert sandwich_cost('wheat', 'chicken', 'no', '', 'yes', 'yes', 'yes', 'no') == 7
    assert sandwich_cost('wheat', 'chicken', 'no', '', 'yes', 'yes', 'no', 'no') == 6.5
    assert sandwich_cost('wheat', 'chicken', 'no', '', 'yes', 'no', 'no', 'no') == 5.5
    assert sandwich_cost('wheat', 'chicken', 'no', '', 'no', 'no', 'no', 'no') == 4.5
