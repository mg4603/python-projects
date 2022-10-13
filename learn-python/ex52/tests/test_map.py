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
    assert central_corridor.go('shoot!') == shoot_death
    assert central_corridor.go('dodge!') == dodge_death
    assert central_corridor.go('tell a joke') is not None and START.go('tell a joke') == laser_weapon_armory

    assert laser_weapon_armory.go('0132') is the_bridge
    assert laser_weapon_armory.go('*') is wrong_pass_death

    assert the_bridge.go('throw the bomb') is throw_bomb_death
    assert the_bridge.go('slowly place the bomb') is escape_pod

    assert escape_pod.go('2') is the_end_winner
    assert escape_pod.go('*') is the_end_loser

    assert START is central_corridor
