import zombiedice
from zombiedice import roll
from random import randint

class MyZombie:
    def __init__(self, name):
        self.name = name
    
    def turn(self, game_state):
        dice_roll_results = roll()
        brains = 0
        while dice_roll_results is not None:
            brains += dice_roll_results['brains']
            if brains < 2:
                dice_roll_results = roll()
            else:
                break

class RandomZombie:
    def __init__(self, name):
        self.name = name
    
    def turn(self, game_state):
        dice_roll_results = roll()
        while dice_roll_results is not None and randint(0, 1) ==0:
            dice_roll_results = roll()

class TwoBrainsZombie:
    def __init__(self, name):
        self.name = name
    
    def turn(self, game_state):
        dice_roll_results = roll()
        brains = 0
        while dice_roll_results is not None:
            brains += dice_roll_results['brains'] 
            if brains >= 2:
                break
            else:
                dice_roll_results = roll()

class TwoShotgunsZombie:
    def __init__(self, name):
        self.name = name

    def turn(self, game_state):
        dice_roll_results = roll()
        shotguns = 0
        while dice_roll_results is not None:
            shotguns += dice_roll_results['shotgun']
            if shotguns > 1 :
                break
            else:
                dice_roll_results = roll()

class OneFourZombie:
    def __init__(self, name):
        self.name = name
    
    def turn(self, game_state):
        dice_roll_results = roll()
        count = randint(1, 4)
        shotguns = 0
        while count and dice_roll_results is not None:
            count -= 1
            shotguns += dice_roll_results['shotgun']
            if shotguns > 1:
                break
            else: 
                dice_roll_results = roll()

zombies = (
    RandomZombie(name='Random'),
    TwoBrainsZombie(name='Stop after 2 brains'),
    TwoShotgunsZombie(name='Stop after 2 shotguns'),
    OneFourZombie(name="Random number of rolls b/w 1-4 or stop after 2 shotguns"),
    zombiedice.examples.RollsUntilInTheLeadZombie(name='Until Leading'),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 2\
    Shotguns', minShotguns=2),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 1\
    Shotgun', minShotguns=1),
    MyZombie(name='My Zombie Bot'),
)

zombiedice.runTournament(zombies=zombies, numGames=1000)
# zombiedice.runWebGui(zombies=zombies, numGames=1000)