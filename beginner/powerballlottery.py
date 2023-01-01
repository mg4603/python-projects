from random import shuffle, randint

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