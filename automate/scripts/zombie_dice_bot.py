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

