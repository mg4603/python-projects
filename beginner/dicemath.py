from time import time, sleep
from random import randint, choice

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

    def display_results(self):
        score = (self.correct_answers * self.REWARD) - \
            (self.incorrect_answers * self.PENALTY)
        print('Correct:   {}'.format(self.correct_answers))
        print('Incorrect: {}'.format(self.incorrect_answers))
        print('Score:     {}'.format(score))

    def main(self):
        input('Press Enter to begin...')

        start_time = time()
        while time() < start_time + self.QUIZ_DURATION:
            sum_answer = 0
            dice_faces = []
            for i in range(randint(self.MIN_DICE, self.MAX_DICE)):
                die = choice(self.ALL_DICE)
                dice_faces.append(die[0])
                sum_answer += die[1]
            
            # list of tuples: (x, y) which are the coordinates of the 
            # top left corner of the dice on the canvas
            top_left_dice_corners = []

            for i in range(len(dice_faces)):
                while True:
                    # find a random place on the canvas to put the dice
                    left = randint(
                        0, self.CANVAS_WIDTH - 1 - self.DICE_WIDTH
                    )
                    top = randint(
                        0, self.CANVAS_HEIGHT - 1 - self.DICE_HEIGHT
                    )

                    top_left_x = left
                    top_left_y = top
                    top_right_x = left + self.DICE_WIDTH
                    top_right_y = top
                    bottom_left_x = left
                    bottom_left_y = top + self.DICE_HEIGHT
                    bottom_right_x = left + self.DICE_WIDTH
                    bottom_right_y = top + self.DICE_HEIGHT

                    overlaps = False
                    for prev_die_left, prev_die_top in top_left_dice_corners:
                        prev_die_right = prev_die_left + self.DICE_WIDTH
                        prev_die_bottom = prev_die_top + self.DICE_HEIGHT
                        for corner_x, corner_y in (
                                (top_left_x, top_left_y),
                                (top_right_x, top_right_y),
                                (bottom_left_x, bottom_left_y),
                                (bottom_right_x, bottom_right_y)
                            ):
                            if (prev_die_left <= corner_x < prev_die_right\
                                    and \
                                    prev_die_top <= corner_y < prev_die_bottom):
                                overlaps = True
                    
                    if not overlaps:
                        top_left_dice_corners.append((left, top))
                        break
            
            # key:tuple - (x, y)
            # value: char at that position on the canvas
            canvas = {}

            for i, (die_left, die_top) in enumerate(top_left_dice_corners):
                die_face = dice_faces[i]
                for dx in range(self.DICE_WIDTH):
                    for dy in range(self.DICE_HEIGHT):
                        canvas_x = die_left + dx
                        canvas_y = die_top + dy
                        canvas[(canvas_x, canvas_y)] = die_face[dy][dx]
            
            for cy in range(self.CANVAS_HEIGHT):
                for cx in range(self.CANVAS_WIDTH):
                    print(canvas.get((cx, cy), ' '), end='')
                print()
            
            response = input('Enter the sum: ').strip()
            if response.isdecimal() and int(response) == sum_answer:
                self.correct_answers += 1
            else:
                print('Incorrect, the answer is {}'.format(
                    sum_answer
                ))
                sleep(2)
                self.incorrect_answers += 1

