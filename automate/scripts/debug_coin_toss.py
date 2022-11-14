from random import choice
from logging import debug, DEBUG, basicConfig, CRITICAL, disable
basicConfig(level=DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# disable(CRITICAL)

def get_input(prompt):
    guess = ''
    while guess not in ('heads', 'tails'):
        guess = input(prompt)
    return guess

def get_toss():
    return choice(('heads', 'tails'))

toss = get_toss()
debug('toss: %s' % toss)
choice = get_input('Guess the coin toss! Enter heads or tails: ')
debug('choice: %s' % choice)

if toss == choice:
    print('You got it!')
else:
    print('Nope! Guess again!')
    choice = get_input('Enter heads or tails: ')
    debug('choice: %s' % choice)
    if toss == choice:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')


