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
from ex43.scenes import *

class Engine:

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()

        while True:
            print("\n-------------------------------------------")
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)



class Map:
    scenes = {
        "central_corridor"      : CentralCorridor(),
        "laser_weapon_armory"   : LaserWeaponArmory(),
        "the_bridge"            : Bridge(),
        "escape_pod"            : EscapePod(),
        "death"                 : Death()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        return Map.scenes.get(scene_name)

    def opening_scene(self):
        return self.next_scene(self.start_scene)
        

a_map = Map("central_corridor")
a_game = Engine(a_map)
a_game.play()