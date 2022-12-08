class DiceMath:
    def __init__(self):
        self.DICE_WIDTH = 9
        self.DICE_HEIGHT = 5
        self.CANVAS_WIDTH = 79
        self.CANVAS_HEIGHT = 24 - 3
        self.QUIZ_DURATION = 30
        self.MIN_DICE = 2
        self.MAX_DICE = 6
        

    def display_intro(self):
        print('---------------------------------------------------------------')
        print('---------------------------Dice Math---------------------------')
        print('---------------------------------------------------------------')
        print()
        print('Add up the sides of all  the dice displayed on the screen. You ')
        print('30 seconds to answer as many as possible. You get 4 points for ')
        print('each correct answer and lose 1 point for each incorrect answer.')
        print()

    def main(self):
        pass