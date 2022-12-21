'''
class LuckyStars
    const:
        STAR_FACE
        SKULL_FACE
        QUESTION_FACE
    
        GOLD
        SILVER
        BRONZE
    
        FACE_WIDTH
        FACE_HEIGHT
    
    attributes:
        player_names
        player_scores
        winners
    
    methods:
        display_intro
        main
        setup_round
        get_players
        display_scores
        get_winner
        display_winner
        ask_continue_turn

'''
from random import shuffle, randint

class LuckyStars:
    STAR_FACE = [
        "+-----------+",
        "|     .     |",
        "|    ,O,    |",
        "| 'ooOOOoo' |",
        "|   `OOO`   |",
        "|   O' 'O   |",
        "+-----------+"
    ]
    SKULL_FACE = [
        "+-----------+",
        "|    ___    |",
        "|   /   \\   |",
        "|  |() ()|  |",
        "|   \\ ^ /   |",
        "|    vvv    |",
        "+-----------+"
    ]
    QUESTION_FACE = [
        "+-----------+",
        "|           |",
        "|           |",
        "|     ?     |",
        "|           |",
        "|           |",
        "+-----------+"
    ]

    GOLD = 'GOLD'
    SILVER = 'SILVER'
    BRONZE = 'BRONZE'

    FACE_WIDTH = 13
    FACE_HEIGHT = 7

    def __init__(self):
        self.player_names = []
        self.player_scores = {}
        self.winners = []
    
    def display_intro(self):
        print('-------------------------------------------------------------')
        print('------------------------ Lucky Stars ------------------------')
        print('-------------------------------------------------------------')
        print()
        print('A "press your luck" game where you roll dice with Stars,')
        print('Skulls, and Question Marks.')
        print()
        print('On your turn, you pull three random dice from the dice cup and')
        print('roll them. You can roll Stars, Skulls and Question Marks. You')
        print('can end your turn and get one point per star. If you choose to')
        print('roll again, you keep the Question Marks and pull new dice to')
        print('replace the Stars, and Skulls. If you collect three Skulls,')
        print('you loose all your stars and end your turn.')
        print()
        print('When a player gets 13 points, everyone else gets one more turn')
        print('before the game ends. Whoever has the most points wins.')
        print()
        print('There are 6 Gold dice, 4 Silver dice, and 3 Bronze dice in the')
        print('cup. Gold dice have more Stars, Bronze dice have more Skulls, ')
        print('and Silver is even.')
        print()

    def get_players(self):
        print('How many players are there?')
        while True:
            response = input('> ')
            if response.isdecimal() and int(response) > 1:
                num_players = int(response)
                break
            print('Please enter a number larger than 1.')

        for i in range(num_players):
            while True:
                print('What is player #{}\'s name?'.format(i + 1))
                player_name = input('> ')
                if player_name != '' and player_name not in self.player_names:
                    self.player_names.append(player_name)
                    self.player_scores[player_name] = 0
                    break
                print('Please enter a name.')
        print()

    def display_scores(self):
        print('SCORES: ', end='')
        for i, name in enumerate(self.player_names):
            if i != 0:
                print(', ', end='')
            print('{} = {}'.format(name, self.player_scores[name]), end='')
        print()

    def get_winner(self):
        hightest_score = 0
        for name in self.player_names:
            if self.player_scores[name] > hightest_score:
                hightest_score = self.player_scores[name]
                self.winners = [name]
            elif self.player_scores[name] == hightest_score:
                self.winners.append(name)

    def display_winner(self):
        if len(self.winners) == 1:
            print('The winner is {}!!!'.format(self.winners[0]))
        else:
            print('The winners are: {}'.format(', '.join(self.winners)))

    def ask_continue_turn(self):
        while True:
            response = input('> ').upper()
            if response != '' and (
                response == 'NO' or response == 'YES' or 
                response == 'Y' or response == 'N'
            ):
                if response == 'NO' or response == 'N':
                    return False
                elif response == 'YES' or response == 'Y':
                    return True
            print('Please enter Yes or No.') 

    def main(self):
        self.display_intro()
        self.get_players()

        turn = 0
        end_game_with = None
        while True:
            self.display_scores()
            
            stars, skulls = 0, 0
            cup = ([self.GOLD] * 6) + ([self.SILVER] * 4) + ([self.BRONZE] * 3)
            hand = []
            print('It is {}\'s turn.'.format(self.player_names[turn]))
            while True:
                print()

                if (3 - len(hand)) > len(cup):
                    print('{} {}\n{}{}'.format(
                        'There aren\'t enough dice left in the cup to',
                        'continue',
                        self.player_names[turn],
                        '\'s turn.'
                    ))
                    self.player_scores[self.player_names[turn]] += stars
                    break

                shuffle(cup)
                while len(hand) < 3:
                    hand.append(cup.pop())
                
                print(hand)
                roll_results = []
                for dice in hand:
                    roll = randint(1, 6)
                    if dice == self.GOLD:
                        if 1 <= roll <= 3:
                            roll_results.append(self.STAR_FACE)
                            stars += 1
                        elif 4 <= roll <= 5:
                            roll_results.append(self.QUESTION_FACE)
                        else:
                            roll_results.append(self.SKULL_FACE)
                            skulls += 1
                    elif dice == self.SILVER:
                        if 1 <= roll <= 2:
                            roll_results.append(self.STAR_FACE)
                            stars += 1
                        elif 3 <= roll <= 4:
                            roll_results.append(self.QUESTION_FACE)
                        else:
                            roll_results.append(self.SKULL_FACE)
                            skulls += 1
                    elif dice == self.BRONZE:
                        if 1 == roll:
                            roll_results.append(self.STAR_FACE)
                            stars += 1
                        elif 2 <= roll <= 3:
                            roll_results.append(self.QUESTION_FACE)
                        else:
                            roll_results.append(self.SKULL_FACE)
                            skulls += 1
                print(len(roll_results))
                for line_num in range(self.FACE_HEIGHT):
                    for dice_num in range(3):
                        print(roll_results[dice_num][line_num], end='')                    
                    print()
                
                for dice_type in hand:
                    print(dice_type.center(self.FACE_WIDTH), end=' ')
                print()

                print('Stars collected: {}  Skulls collected: {}'.format(
                    stars, skulls
                ))

                if skulls >= 3:
                    print('3 or more skulls mean\'s you\'ve lost your stars!')
                    input('Press Enter to continue...')
                    break

                print('{} do you want to roll again? Y/N'.format(
                    self.player_names[turn]
                ))
                continue_turn = self.ask_continue_turn()

                if not continue_turn:
                    print('{} got {} stars!'.format(
                        self.player_names[turn],
                        stars
                    ))
                    self.player_scores[self.player_names[turn]] += stars
              
                    if (end_game_with == None and
                        self.player_scores[self.player_names[turn]] >= 13):
                        print(f'\n\n{"!" * 60}')
                        print('{} has reached 13 points!!!'.format(
                            self.player_names[turn]
                        ))
                        print('Everyone else will get one more turn!')
                        print(f'{"!" * 60}\n\n')
                        end_game_with = self.player_names[turn]
                    input('Press Enter to continue...')
                    break

                
                next_hand = []
                for i in range(3):
                    if roll_results[i] == self.QUESTION_FACE:
                        next_hand.append(hand[i])
                
                hand = next_hand
        
            turn = (turn + 1) % len(self.player_names)

            if end_game_with == self.player_names[turn]:
                break

        print('The game has ended...')
        self.display_scores()

        self.get_winner()
        self.display_winner()
        print('Thanks for playing!')

if __name__ == '__main__':
    game = LuckyStars()
    game.main()