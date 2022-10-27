from scripts.mcb import (
 save_shelf, load_shelf   
)

def test_shelf():
    save_shelf('new', 'first clip')
    assert load_shelf() == {'new':'first clip'}