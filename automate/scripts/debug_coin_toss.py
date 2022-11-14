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

