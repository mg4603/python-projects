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

    def setup_round(self):
        pass

    def main(self):
        pass

    def get_players(self):
        pass

    def display_scores(self):
        pass

    def get_winner(self):
        pass

    def display_winner(self):
        pass

    def ask_continue_turn(self):
        pass