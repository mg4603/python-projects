class DiceMath:
    def __init__(self):
        self.DICE_WIDTH = 9
        self.DICE_HEIGHT = 5
        self.CANVAS_WIDTH = 79
        self.CANVAS_HEIGHT = 24 - 3
        self.QUIZ_DURATION = 30
        self.MIN_DICE = 2
        self.MAX_DICE = 6
        self.REWARD = 4
        self.PENALTY = 1
        assert self.MAX_DICE <= 14
        self.D1 = (
            [
                '+-------+',
                '|       |',
                '|   0   |',
                '|       |',
                '+-------+'
            ], 1
        )
        self.D2a = (
            [
                '+-------+',
                '| 0     |',
                '|       |',
                '|     0 |',
                '+-------+'
            ], 2
        )

    def display_intro(self):
        print('---------------------------------------------------------------')
        print('---------------------------Dice Math---------------------------')
        print('---------------------------------------------------------------')
        print()
        print('Add up the sides of all  the dice displayed on the screen. You ')
        print(
            '{} seconds to answer as many as possible. You get {} points for '.format(
                self.QUIZ_DURATION, self.REWARD
            )
        )
        print(
            'each correct answer and lose {} point for each incorrect answer.'.format(
                self.PENALTY
            )
        )
        print()

    def main(self):
        pass