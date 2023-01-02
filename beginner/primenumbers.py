from math import sqrt
from sys import exit

class PrimeNumbers:
    def __init__(s):
        pass
    
    def is_prime(s, num):
        if num < 2:
            return False
        elif num == 2:
            return True

        for i in range(2, int(sqrt(num)) + 1):
            if num % i == 0:
                return False
        
        return True