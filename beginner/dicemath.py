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
        self.D2b = (
            [
                '+-------+',
                '|     0 |',
                '|       |',
                '| 0     |',
                '+-------+'
            ], 2
        )
        self.D3a = (
            [
                '+-------+',
                '| 0     |',
                '|   0   |',
                '|     0 |',
                '+-------+'
            ], 3
        )
        self.D3b = (
            [
                '+-------+',
                '|     0 |',
                '|   0   |',
                '| 0     |',
                '+-------+'
            ], 3
        )
        self.D4 = (
            [
                '+-------+',
                '| 0   0 |',
                '|       |',
                '| 0   0 |',
                '+-------+'
            ], 4
        )
        self.D5 = (
            [
                '+-------+',
                '| 0   0 |',
                '|   0   |',
                '| 0   0 |',
                '+-------+'
            ], 5
        )
        self.D6a = (
            [
                '+-------+',
                '| 0 0 0 |',
                '|       |',
                '| 0 0 0 |',
                '+-------+'
            ], 6
        )
        self.D6b = (
            [
                '+-------+',
                '| 0   0 |',
                '| 0   0 |',
                '| 0   0 |',
                '+-------+'
            ], 6
        )
        self.ALL_DICE = [
            self.D1, self.D2a, self.D2b, self.D3a, self.D3b, 
            self.D4, self.D5, self.D6a, self.D6b
        ]
        self.correct_answers = 0
        self.incorrect_answers = 0

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