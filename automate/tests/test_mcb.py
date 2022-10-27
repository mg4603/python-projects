from scripts.mcb import (
 delete_from_shelf, save_shelf, load_shelf   
)

def test_shelf():
    save_shelf('new', 'first clip')
    assert load_shelf() == {'new':'first clip'}

def test_delete_from_shelf():
    save_shelf('new2', 'second clip')
    assert load_shelf() == {'new': 'first clip', 'new2': 'second clip'}
    delete_from_shelf('new2')
    assert load_shelf() == {'new': 'first clip'}