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
        pass