"""
Text Description:
Aliens have invaded a spaceship and our hero has to go through a maze of rooms 
defeating them so he can escape into an escape pod to the planet below. The game
will be more like a Zork or Adventure type game with text outputs and funny ways
die. The game will involve an engine that runs a map full of rooms or scenes. 
Each room will print it's own description when the player enters it and then tell
the engine what room to run next out of the map.

Scenes:
    Death                   :   This is when the player dies and should be something
                                funny.

    Central Corridor        :   This is the starting point and has a gothon already.
                                standing, which the player has to defeat with a joke 
                                before continuing.

    Laser Weapon Armory     :   This is where the player gets a neutron bomb to 
                                blow up the ship before getting to the escape pod.
                                It has a keypad he has to guess the number for.
    
    The Bridge              :   Another battle scene with a gothon where the player
                                places the bomb.
    
    Escape Pod              :   Where the player escapes, but only after guessing the
                                right escape pod.

Keywords:
    - Alien
    - Player
    - Maze
    - Map
    - Planet
    - Gothon
    - Spaceship
    - Engine
    - Escape pod
    - Death
    - Central Corridor
    - Laser Weapon Armory
    - The Bridge
    - Player
    - Game
    - Room


Class Hierarchy:
    * Map
        - next_scene
        - opening_scene
    * Engine
        - play
    * Scene
        - enter
        * Death
        * CentralCorridor
        * LaserWeaponArmory
        * Bridge
        * EscapePod

    
"""

from sys import exit
from random import randint

class Scene:

    def enter(self):
        print("This scene is not yet configured. Subclass it and implement enter().")
        exit(1)

class Engine:

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()

        while True:
            print("\n-------------------------------------------")
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)


class Death:
    
    def enter(self):
        pass


class CentralCorridor:

    def enter(self):
        pass

class LaserWeaponArmory:

    def enter(self):
        pass


class Bridge:

    def enter(self):
        pass


class EscapePod:

    def enter(self):
        pass


class Map:

    def __init__(self, start_scene):
        pass

    def next_scene(self, scene_name):
        pass

    def opening_scene(self):
        pass


a_map = Map("central_corridor")
a_game = Engine(a_map)
a_game.play()