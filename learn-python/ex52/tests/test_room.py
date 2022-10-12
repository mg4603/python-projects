from app.modules.room import Room

def test_room():
    gold = Room("GoldRoom",
                """This room has gold in it you can grab. There's a door
                to the north.""")
    assert gold.name == "GoldRoom"
    assert gold.paths == {}

