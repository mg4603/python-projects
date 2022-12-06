class CarrotInBox:
    def __init__(self, player1, player2):
        self.player1 = ''
        self.player2 = ''
    
    def display_intro(self):
        print('-------------------------Carrot In A Box-------------------------')
        print('\nA silly bluffing game between two human players. Based on the ')
        print('game from the show: 8 out of 10 cats')
        print()
        print('This is a bluffing game for two human players. Each player has a ')
        print('box. One box has a carrot in it. To win, you must have the box with')
        print('the carrot in it.')
        print()
        print('This is a very simple and silly game.')
        print()
        print('The first player looks into their box (the second player must close')
        print('their eyes during this). The first player then says "There is a ')
        print('carrot in my box" or "There is not a carrot in my box". The second')
        print('player then gets to decide if they want to swap boxes or not.')