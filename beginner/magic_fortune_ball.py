'''
const:
    REPLIES = [
        'let me think on this...',
        'an interesting question...',
        'hmm...are you sure you want to know..?',
        'do you think some things are best left unknown..?',
        'i might tell you, but you might not like the answer...',
        'yes... no... maybe... i will think on it...',
        'and what will you do when you know the answer? we shall see...',
        'i shall consult my vision...',
        'you may want to sit down for this...'
    ]
    ANSWERS = [
        'yes, for sure',
        'my answer is no',
        'ask me later',
        'i am programmed to say yes',
        'the stars say yes, but i say no',
        'i dunno maybe',
        'focus and ask once more',
        'doubtful, very doubtful',
        'affirmative',
        'yes, thought you may not like it',
        'no, but you may wish it was so'
    ]
methods:
    main
    slow_space_print
'''
from time import sleep
from random import choice, randint

class MagicFortuneBall:
    REPLIES = [
        'let me think on this...',
        'an interesting question...',
        'hmm...are you sure you want to know..?',
        'do you think some things are best left unknown..?',
        'i might tell you, but you might not like the answer...',
        'yes... no... maybe... i will think on it...',
        'and what will you do when you know the answer? we shall see...',
        'i shall consult my vision...',
        'you may want to sit down for this...'
    ]
    ANSWERS = [
        'yes, for sure',
        'my answer is no',
        'ask me later',
        'i am programmed to say yes',
        'the stars say yes, but i say no',
        'i dunno maybe',
        'focus and ask once more',
        'doubtful, very doubtful',
        'affirmative',
        'yes, thought you may not like it',
        'no, but you may wish it was so'
    ]
    def __init__(self):
        pass

    def slow_space_print(self, msg, time_interval=0.1):
        msg = msg.lower()
        for char in msg:
            if char == 'i':
                print(char, end=' ', flush=True)
            else:
                print(char.upper(), end=' ', flush=True)
            sleep(time_interval)
        print()
        print()

    def main(self):
        self.slow_space_print('magic fortune ball')
        sleep(0.5)
        self.slow_space_print('ask me your yes/no question.')
        input('> ')

        self.slow_space_print(choice(self.REPLIES))
        self.slow_space_print('.' * randint(4, 12), 0.7)

        self.slow_space_print('I have an answer...', 0.2)
        sleep(1)
        self.slow_space_print(choice(self.ANSWERS))

if __name__ == '__main__':
    fortune_ball = MagicFortuneBall()
    fortune_ball.main()