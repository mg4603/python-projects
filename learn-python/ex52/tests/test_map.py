from app.modules.room import Room
from app.modules.map import *

def test_paths():
    start = Room("Start", "You can go west and down a hole.")
    west = Room("West", "There are trees here you can go east.")
    down = Room("Down", "It's dark down here, you can go up.")

    start.add_paths({"west": west,
                     "down": down})
    west.add_paths({"east": start})
    down.add_paths({"up": start})

    assert start.go("west") == west
    assert start.go("west").go("east") == start
    assert start.go("down").go("up") == start

def test_gothon_game_map():
    assert START.go('shoot!') == the_end_loser.setMessage(throw_bomb_death)
    assert START.go('dodge!') == the_end_loser.setMessage(dodge_death)

    room = START.go('tell a joke')
    assert room == laser_weapon_armory

    