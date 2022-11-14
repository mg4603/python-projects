from random import choice

def get_input(prompt):
    guess = ''
    while guess not in ('heads', 'tails'):
        guess = input(prompt)

def get_toss():
    return choice(('heads', 'tails'))

