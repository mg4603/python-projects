from app.modules.room import Room

def test_room():
    gold = Room("GoldRoom",
                """This room has gold in it you can grab. There's a door
                to the north.""")
    assert gold.name == "GoldRoom"
    assert gold.paths == {}

def test_room_go_add_paths():
    center = Room("Center", "Test room in the center.")
    north = Room("North", "Test room in the north.")
    south = Room("South", "Test room in the south.")

    center.add_paths({"north": north,
                    "south": south})
    
    assert center.go("north") == north
    assert center.go("south") == south
