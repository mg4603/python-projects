from time import sleep
from sys import exit

class Collatz:
    def __init__(self, number):
        self.number = number

    def display_intro(self):
        print('--------------------------------------------------------------')
        print('-----------Collatz Sequence, or, the 3n + 1 Problem-----------')
        print('--------------------------------------------------------------')
        print('The collatz sequence is a sequence of numbers produced from a ')
        print('starting number n, following three rules:')
        print('\t1) If n is even, the next number n is n/2')
        print('\t2) If n is odd, the next number n is 3 * n + 1')
        print('\t3) If n is 1, stop. Otherwise, repeat')
        print()
        print("It is generally thought, but so far not mathematically proven,")
        print('that every starting number eventually terminates at 1.')
        print()
    
    def main(self):
        print(self.number, end='', flush=True)
        while self.number != 1:
            if self.number % 2 == 0:
                self.number = self.number // 2
            else:
                self.number = 3 * self.number + 1

            print(f', {self.number}', end='', flush=True)
            sleep(0.1)
        print()

def get_initial_number():
    print('Enter a starting number (greater than 0) or QUIT')
    while True:
        response = input('> ').upper()

        if response == 'QUIT':
            exit()
        elif not response.isdecimal() or response == '0':
            print('You must enter an integer greater than 0')
        else:
            return int(response)

if __name__ == '__main__':
    number = get_initial_number()
    collatz = Collatz(number)
    collatz.display_intro()
    collatz.main()
