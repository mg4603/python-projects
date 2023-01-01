from random import shuffle, randint
from sys import exit

class PowerballLottery:
    def __init__(s, numbers, powerball):
        assert type(powerball) == int
        assert 1 <= powerball <= 26, \
            'Powerball must be between 1 and 26'
        for num in numbers:
            assert type(num) == int, \
                'All members of list must be numbers.'
            assert 1 <= num <= 69, \
                'All members of list must be between 1 and 69.'
        assert len(numbers) == 5, 'List of 5 numbers required.'

        s.numbers = numbers
        s.powerball = powerball
        s.possible_numbers = list(range(1, 70))

    def display_intro(s):
        print('Powerball Lottery')
        print()
        print('Each powerball lottery ticket costs $2. The jackpot for')
        print('This game is $1.586 billion! It doesn\'t matter what the')
        print('jackpot is, though, because the odds are 1 in 292,201,338,')
        print('so you won\'t win.')
        print()
        print('This simulation gives you the thrill of playing without')
        print('wasting money.')
        print()
    
    def simulate(s):
        shuffle(s.possible_numbers)
        winning_numbers = s.possible_numbers[0:5]
        winning_powerball = randint(1, 26)

        print('The winning numbers are: ', end='')
        winning_numbers_str = ' '.join(
            [str(num) for num in winning_numbers]
        ) + ' and ' + str(winning_powerball)
        print(winning_numbers_str.ljust(21), end='')
        
        if set(winning_numbers) == set(s.numbers)\
                and winning_powerball == s.powerball:
            print()
            print('You have won the Powerball lottery! Congratulations,')
            print('you would have been a billionaire if this was real!')
            return
        else:
            print(' You lost!')

def get_numbers():
    while True:
        print('Enter 5 different numbers from 1 to 69, with spaces between')
        print('each number. (For example: 5 17 21 35 10)')
        response = input('> ')

        numbers = response.split(' ')
        if len(numbers) != 5:
            print('Please enter 5 numbers, separated by spaces.')
            continue

        try:
            for i in range(5):
                numbers[i] = int(numbers[i])
        except ValueError:
            print('Please enter numbers like 26, 14 or 1')
            continue

        for num in numbers:
            if not 1 <= num <= 69:
                print('The numbers must all be between 1 and 69.')
                continue
        
        if len(set(numbers)) != 5:
            print('You must enter 5 different numbers.')
            continue

        return numbers

def get_powerball():
    while True:
        print('Enter the powerball number from 1 to 26.')
        response = input('> ')

        try:
            powerball = int(response)
        except ValueError:
            print('Please enter a number like 1, 2, or 24.')
            continue
        
        if not 1 <= powerball <= 26:
            print('The powerball number must be between 1 and 26.')
            continue

        return powerball

def get_num_of_play():
    while True:
        print('How many times do you want to play? (Max: 1,000,000)')
        response = input('> ')

        try:
            num_plays = int(response)
        except ValueError:
            print('Please enter a number, like 1, 5, 10 or 30000')
            continue

        if not 1 <= num_plays <= 1_000_000:
            print('You can play between 1 and 1,000,000 times.')
            continue

        return num_plays

def main():
    numbers = get_numbers()
    powerball = get_powerball()
    num_plays = get_num_of_play()
    game = PowerballLottery(numbers, powerball)
    price = num_plays * 2
    print('It costs ${} to play {} times, but don\'t worry.'.format(
        price, num_plays
    ))
    print('I\'m sure you\'ll win it all back.')
    input('Press Enter to start...')
    for i in range(num_plays):
        game.simulate()
    print('You wasted ${}'.format(price))
    print('Thanks for playing!')

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()