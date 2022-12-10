from sys import exit
from math import sqrt

class FactorFinder:
    def __init__(self, number):
        if is_int(number):
            self.number = number
        else:
            raise Exception('Number to factorize needs to be an integer.')
        
        self.factors = []

    def display_intro(self):
        print('-------------------------------------------------------------')
        print('------------------------Factor Finder------------------------')
        print('-------------------------------------------------------------')
        print()
        print('A number\'s factors are two numbers that, when multiplied with')
        print('each other, produce the number. For example 2 x 13 = 26, so ')
        print('2 and 13 are factors of 26. 1 x 26 = 26, so 1 and 26 are also')
        print('factors of 26. We say that 26 has four factors: 1, 2, 13 and26.')
        print()
        print('If a number only has two factors (1 and itself), we call that a')
        print('prime number.Otherwise, we call it a composite number.')
        print()
        print('Can you discover some prime numbers?')

    def factorize(self):
        is_neg = False
        if self.number < 0:
            is_neg = True
            self.number = -self.number

        for num in range(1, int(sqrt(self.number)) + 1):
            if self.number % num == 0:
                self.factors.append(num)
                self.factors.append(self.number // num)

        if is_neg:
            for factor in self.factors:
                self.factors.append(-factor)

        self.factors = list(set(self.factors))

        self.factors.sort()

    def display_factors(self):
        print('Factors to {} are: '.format(self.number))
        print(', '.join(self.factors))

def is_int(num):
    try:
        int(num)
        if num % 1 != 0:
            return False
        return True
    except:
        return False

def handle_inputs():
    print('Enter a number to factor (or "QUIT" to quit)')
    while True:
        response = input('> ').replace(' ', '').strip()
        if response.upper() == 'QUIT':
            exit()
        if is_int(response):
            return int(response)
        else:
            print('Number to factorize needs to be an integer.')

if __name__ == '__main__':
    while True:
        number = handle_inputs()
        factor_finder = FactorFinder(number)
        factor_finder.factorize()
        factor_finder.display_factors()