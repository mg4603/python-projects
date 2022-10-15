import zombiedice

class MyZombie:
    def __init__(self, name):
        self.name = name
    
    def turn(self, game_state):
        dice_roll_results = zombiedice.roll()
        brains = 0
        while dice_roll_results is not None:
            brains += dice_roll_results['brains']
            if brains < 2:
                dice_roll_results = zombiedice.roll()
            else:
                break

class RandomZombie:
    def __init__(self, name):
        self.name = name

zombies = (
    zombiedice.examples.RandomCoinFlipZombie(name='Random'),
    zombiedice.examples.RollsUntilInTheLeadZombie(name='Until Leading'),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 2\
    Shotguns', minShotguns=2),
    zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 1\
    Shotgun', minShotguns=1),
    MyZombie(name='My Zombie Bot'),
)

# zombiedice.runTournament(zombies=zombies, numGames=1000)
zombiedice.runWebGui(zombies=zombies, numGames=1000)