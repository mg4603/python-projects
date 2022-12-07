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
    
    