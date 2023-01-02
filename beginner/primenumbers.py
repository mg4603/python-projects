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
    