from random import randint

def get_input(prompt):
    guess = ''
    while guess not in ('heads', 'tails'):
        guess = input(prompt)

