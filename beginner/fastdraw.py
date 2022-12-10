from time import sleep, time
from random import randint

class FastDraw:
    def __init__(self):
        pass

    def display_intro(self):
        print('-------------------------------------------------------------')
        print('--------------------------Fast Draw--------------------------')
        print('-------------------------------------------------------------')
        print('Time to test your reflexes and see if you are the fastest ')
        print('draw in the west!')
        print('When you see "DRAW" you have 0.3 seconds to press Enter.')
        print('But you lose if you press Enter before "DRAW" appears.')
        print()

    def main(self):
        input('Press Enter to begin...')
        while True:
            print()
            print('It\'s high noon...')
            sleep(randint(20, 50)/ 10.0)
            print('DRAW!')
            draw_time = time()
            input()
            time_elapsed = time() - draw_time
            
            if time_elapsed < 0.1:
                print('You drew before "DRAW" appeared! You lose.')
            elif time_elapsed > 0.3:
                time_elapsed = round(time_elapsed, 4)
                print('You took {} seconds to draw. Too slow!'.format(
                    time_elapsed
                ))
            else:
                time_elapsed = round(time_elapsed, 4)
                print('You took {} seconds to draw.'.format(time_elapsed))
                print('You are the fastest draw in the west! You win!')
            
            while True:
                print('Enter QUIT to stop or press Enter to play again.')
                response = input('> ').upper()
                if response == 'QUIT':
                    print('Thanks for playing!')
                    exit()
                elif response == '':
                    break
                
if __name__ == '__main__':
    game = FastDraw()
    game.display_intro()
    game.main()