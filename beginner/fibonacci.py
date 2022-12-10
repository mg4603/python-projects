from sys import exit

class Fibonacci:
    def __init__(self, nth):
        if not (is_int(nth) and int(nth) > 0):
            raise Exception('Number needs to an integer larger than zero.')
        else:
            self.nth = int(nth)
    
    def display_intro():
        print('--------------------------------------------------------------')
        print('----------------------Fibonacci Sequence----------------------')
        print('--------------------------------------------------------------')
        print()
        print('The Fibonacci sequence begins with 0 and 1, and the next')
        print('number is the sum of the previous two numbers. The sequence')
        print('continues forever: ')
        print()
        print('{}\n{}\n\n'.format(
                '0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377,',
                '610, 987, 1597...'))
    
    def main(self):
        print('Fibonacci sequence:')
        if self.nth == 1:
            print('0')
            print()
            print('The #1 Fibonacci number is 0.')
        elif self.nth == 2:
            print('0, 1')
            print()
            print('The #2 Fibonacci number is 1')

        if self.nth > 10_000:
            print('WARNING: This will take a while to display on the screen.')        
            print('If you wan\'t to quit this program before it is done, ')
            print('press CTRL-C.')
            print('Press Enter to begin...')
        
        second_to_last_number = 0
        last_number = 1
        fib_numbers_calculated = 2
        print('0, 1, ', end='')
        while True:
            next_number = second_to_last_number + last_number
            fib_numbers_calculated += 1

            print(next_number, end="")

            if fib_numbers_calculated == self.nth:
                print('\n\nThe #{} Fibonacci number is {}\n\n'.format(
                    self.nth, next_number
                ))
                break

            print(', ', end='')

            second_to_last_number = last_number
            last_number = next_number

def is_int(number):
    try:
        number = int(number)
        if number % 1 != 0:
            return False
        return True
    except:
        return False

def handle_inputs():
    print('Enter the nth Fibonacci number you wish to calculate')
    print('(such as 5, 50, 1000, 9999), or QUIT to quit:')
    while True:
        response = input('> ').strip().upper()

        if response == 'QUIT':
            print('Thanks for playing!')
            exit()
        
        if is_int(response) and int(response) > 0:
            return int(response)
        print('Enter an integer greater than 0, or QUIT.')

if __name__ == '__main__':
    Fibonacci.display_intro()
    while True:
        number = handle_inputs()
        generator = Fibonacci(number)
        generator.main()