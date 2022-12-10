from sys import exit

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

    def factorize(self):
        pass

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
    print('Enter a number to factor (or "QUIT" to quit')
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