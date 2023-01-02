from math import sqrt
from sys import exit

class PrimeNumbers:
    def __init__(s):
        s.start = 0
    
    def is_prime(s, num):
        if num < 2:
            return False
        elif num == 2:
            return True

        for i in range(2, int(sqrt(num)) + 1):
            if num % i == 0:
                return False
        
        return True
    
    def get_start(s):
        print('Enter a number to start searching for primes from:')
        print('(Try 0 or 100 or another number.)')
        while True:
            response = input('> ')
            if response.isdecimal():
                s.start = int(response)
                return
            print('Input should be a number.')
    
    def display_intro(s):
        print('Prime Numbers')
        print('Prime numbers are numbers that are only evenly divisible by')
        print('one and themselves. They are used in a variety of practical')
        print('applications, but cannot be predicted. They must be')
        print('calculated one at a time.')
        print()
    
    def main(s):
        s.display_intro()
        s.get_start()

        input('Press CTRL-C at any time to quit. Press enter to begin...')

        num = s.start
        while True:
            if s.is_prime(num):
                print(num, end=', ', flush=True)
            num += 1    
    
