from random import randint

class CarrotInBox:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
    
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
    
    def display_closed_boxes(self,first_box, second_box):
        print(f'''
HERE ARE THE TWO BOXES:
  __________    __________
 /         /|  /         /|
+---------+ | +---------+ |
|   {first_box}  | | |   {second_box}  | |
|   BOX   | / |   BOX   | / 
+---------+/  +---------+/''')

    def display_player_names(self):
        print(f'{self.player1[:12].center(12)}{self.player2[:12].center(12)}')
        print()

    def display_first_box(self, carrot_in_fist_box, first_box, second_box):
        if not carrot_in_fist_box:
            print(f'''
   _________
  |         |
  |         |
  |_________|   __________
 /         /|  /         /|
+---------+ | +---------+ |
|   {first_box}  | | |   {second_box}  | |
|   BOX   | / |   BOX   | /
+---------+/  +---------+/
(no carrot!)''')
        else:
            print(f'''
   ___VV____
  |   VV    |
  |   VV    |
  |___||____|   __________
 /    ||   /|  /         /|
+---------+ | +---------+ |
|   {first_box}  | | |   {second_box}  | |
|   BOX   | / |   BOX   | /
+---------+/  +---------+/
 (carrot!)''')

    def display_winner(self, carrot_in_first_box):
        if carrot_in_first_box:
            winner = self.player1
        else:
            winner = self.player2
        print(f'{winner.title()} is the winner!')

    def display_open_boxes(self, carrot_in_first_box, first_box, second_box):
        pass

    def game(self):
        input('Press enter to begin...')

        first_box = 'RED '
        second_box = 'GOLD'

        self.display_closed_boxes(first_box, second_box)
        print()
        self.display_player_names()
        print()
        print(f'{self.player1}, you have a RED box in front of you.')
        print(f'{self.player2}, you have a GOLD box in front of you.')
        print()
        print(f'{self.player1}, you will get to look into your box.')
        print(f'{self.player2.upper()}, close your eyes and don\'t look!!!')
        input(f'When {self.player2} has closed their eyes, press Enter...')
        print()

        print(f'{self.player1} here is the inside of your box:')

        if randint(1, 2) == 1:
            carrot_in_first_box = True
        else:
            carrot_in_first_box = False
        
        self.display_first_box(carrot_in_first_box, first_box, second_box)
        self.display_player_names()

        input('Press Enter to continue...')

        print('\n'*100)
        print(f'{self.player1} tell {self.player2} to open their eyes.')
        input('Press Enter to continue...')

        print()
        print(f'{self.player1}, say one of the following sentences to {self.player2}.')
        print('\t1) There is a carrot in my box.')
        print('\t2) There is not a carrot in my box.')
        print()
        input('Then press Enter to continue...')

        print() 
        print(f'{self.player2}, do you want to swap boxes with {self.player1}? YES/NO')
        while True:
            response = input('> ').upper()
            if not (response.startswith('Y') or response.startswith('N')):
                print(f'{self.player2}, please enter "YES" or "NO".')
            else:
                break
        
        if response.startswith('Y'):
            carrot_in_first_box = not carrot_in_first_box
            first_box, second_box = second_box, first_box

        self.display_closed_boxes(first_box, second_box)
        self.display_player_names()

        input('Press Enter to reveal the winner...')
        print()

        self.display_open_boxes(carrot_in_first_box, first_box, second_box)
        self.display_player_names()

        self.display_winner(carrot_in_first_box)

        print('Thanks for playing!')
