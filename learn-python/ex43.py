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
    quips = [
            "You died. You kinda suck at this.",
            "Your mom would be proud...if she were smarter.",
            "Such a luser.",
            "I have a small puppy that's better at this."
    ]
    def enter(self):
        print(Death.quips[randint(0, len(Death.quips)-1)])    
        exit(0)


class CentralCorridor:

    def enter(self):
        print("The Gothons of Planet Percal #25 have invaded your ship and destroyed")
        print("your entire crew. You are the last surviving member and your last")
        print("mission is to get the neutron destruct bomb from the Weapons Armory,")
        print("put it in the bridge, and blow the ship up after getting into an")
        print("escape pod.\n")
        print("You're running down the central corridor to the Weapons Armory when")
        print("a Gothon jumps out, red scaly skin, dark grimy teeth, and evil clown")
        print("costume flowing around his hate filled body. He is blocking the door")
        print("to the Weapons Armory and is about to pull out a weapon to blast you.")

        action = input("> ")

        if(action == "shoot"):
            print("Quick on the draw you yank out your blaster and fire at the Gothon.")
            print("His clown costumer is flowing and moving around his body, which throws")
            print("off your aim. You laser hits his costume but misses him entirely.")
            print("This completely ruins his brand new costume that his mother bought")
            print("him, which makes him fly into a rage and blast you repeatedly in")
            print("the face until you are ded. Then he eats you.")
            return "death"
        elif(action == "dodge"):
            print("Like a world class boxer, you dodge, weave, slip and slide right as")
            print("the Gothon's blaster cranks a laser past your head.")
            print("In the middle of your artful dodging your foot slips and you bang")
            print("your head on the metal wall and pass out.")
            print("You wake up shortly after, only to die as the Gothon stomps on your")
            print("head and eats you.")
            return "death"
        elif(action == "tell a joke"):
            print("Lucky for you they made you learn Gothon insults in the academy.")
            print("You tell the one Gothon joke you know:")
            print("bhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr, fur fvgf\
            \nnebhaq gur ubhfr.")
            print("The Gothon stops, tries not to laugh, then bursts out laughing and")
            print("can't move. While he's laughing you run up and shoot him square in")
            print("the head putting him down, the jump through the Weapons Armory door.")
            return "laser weapon armory"
        else:
            print("DOES NOT COMPUTE")
            return "central corridor"


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