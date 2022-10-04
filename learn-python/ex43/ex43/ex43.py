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

def isNum(num):
    try:
        int(num)
        return True
    except ValueError:
        return False

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
            print("the head putting him down, then jump through the Weapons Armory door.")
            return "laser_weapon_armory"
        else:
            print("DOES NOT COMPUTE")
            return "central_corridor"


class LaserWeaponArmory:

    def enter(self):
        print("You do a dive roll into the Weapon Armory, crouch and scan the room")
        print("For more Gothons that might be hiding. It's dead quiet, too quiet.")
        print("You stand up and run to the far side of the room and find the ")
        print("neutron bomb in its container. There's a keypad lock on the box")
        print("And you need the code to get it out. If you get the code wrong 10 times")
        print("the lock closes forever and you can't get the bomb. The code is 3")
        print(" digits.")

        code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
        guesses = 0

        guess = input("[keypad]> ")

        while(guesses < 9 and guess != "141" and guess != code):
            print("BZZZZED!")
            guesses += 1
            guess = input("[keypad]> ")
        
        if(guess == code or guess == "141"):
            print("The container clicks open and the seal breaks, letting gas out.")
            print("You grab the neutron bomb and run as fast as you can to the")
            print("bridge where you place it in the right spot.")
            return "the_bridge"
        else:
            print("The lock buzzes one last time and then you hear a sickening")
            print("melting sound as the mechanism fuses together.")
            print("You decide to sit there and finally the Gothons blow up the ")
            print("ship from their ship and you die.")
            return "death"


class Bridge:

    def enter(self):
        print("You burst onto the Bridge with the neutron destruct bomb")
        print("under your arm and surprise 5 Gothons who are trying to")
        print("take control of the ship. Each of them has an even uglier")
        print("clown costume than the last. They haven't pulled out their")
        print("weapons yet as they see the activated bomb under your arm")
        print("and don't want to set it off.")

        action = input("> ")
        
        if(action == "throw the bomb"):
            print("In a panic you throw the bomb at the Gothons and make")
            print("a leap for the door. Right as you throw it a Gothon")
            print("shoots you right in the back killing you. As you die,")
            print("you see another Gothon frantically try to disarm the bomb")
            print("You die knowing that they will probably blow up when it")
            print("goes off.")
            return "death"
        elif(action == "slowly place the bomb"):
            print("You point the blaster at the bomb under your arm and the Gothons")
            print("put their hands up and start to sweat. You inch backwards towards")
            print("the door, open it, and then carefully place it on the floor, ")
            print("pointing your blaster at it. You then jump back through the door,")
            print("punch the close button, and blast the lock so the Gothons can't")
            print("get out. Now that the bomb is placed you run to the escape pod")
            print("to get off this tin can.")
            return "escape_pod"
        else:
            print("DOES NOT COMPUTE")
            return "the_bridge"


class EscapePod:

    def enter(self):
        print("You rush through the ship, desperately trying to make it")
        print("to the escape pod before the whole ship explodes. It seems")
        print("like hardly any Gothons are on the ship, so your run is ")
        print("clear of interference. You get to the chamber with escape")
        print("pods, and now need to pick one to take. Some of them could")
        print("be damaged but you don't have time to look. There's 5 pods,")
        print("which one do you take?")

        good_pod = randint(1, 5)
        guess = input("[pod#]> ")


        while(not isNum(guess)):
            print("Learn to type a number.")
            guess = input("[pod#]> ")

        if(int(guess) != good_pod):
            print("You jump into pod %s and hit the eject button." % guess)
            print("The pod escapes out into the void of space, then")
            print("implodes as the hull ruptures, crushing your body")
            print("into jam jelly.")
            return "death"
        else:
            print("You jump into pod %s and hit the eject button." % guess)
            print("The pod easily slides out into space heading to the")
            print("planet below. As it flies to the planet, you look")
            print("back and see your ship implode and explode like a ")
            print("bright star, taking out the Gothon ship at the same time.")
            print("You won!")
            return "finished"


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