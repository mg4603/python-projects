from sys import exit
from random import choice, randint
from time import sleep

try:
    from bext import clear, size, bg
except ImportError:
    print('This program requires the bext module.')
    print(
        'Find installation instructions at https://pypi.org/project/Bext/'
    )
    exit()

NUM_FISH = 10
NUM_KELP = 2
NUM_BUBBLERS = 1

class FishTank:
    WIDTH, HEIGHT = size()
    FRAMES_PER_SECOND = 4

    FISH_TYPES = [
        {
            'right': ['><>'],
            'left': ['<><'],
        },
        {
            'right': ['>||>'],
            'left': ['<||<']
        },
        {
            'right': ['>))>'],
            'left': ['<((<']
        },
        {
            'right': ['>||o', '>||.'],
            'left': ['o||<', '.||<']
        },
        {
            'right': ['>))o', '>)).'],
            'left': ['o((<', '.((<']
        },
        {
            'right': ['>-==>'],
            'left': ['<==-<']
        },
        {
            'right': [r'>\\>'],
            'left': ['<//<']
        },
        {
            'right': ['><)))*>'],
            'left': ['<*(((><']
        },
        {
            'right': ['}-[[[*>'],
            'left': ['<*]]]-{']
        },
        {
            'right': [']-<)))b>'],
            'left': ['<d(((<-[']
        },
        {
            'right': ['><XXX*>'],
            'left': ['<*XXX><']
        },
        {
            'right': [
                '_.-._.^=>', '.-._.-.^=>',
                '-._.-._^=>', '._.-._.^=>'
            ],
            'left': [
                '<=^._.-._', '<=^.-._.-.',
                '<=^_.-._.-', '<=^._.-._.'
            ]
        }

    ]

    LONGEST_FISH_LENGTH = 10
    LEFT_EDGE = 0
    RIGHT_EDGE = WIDTH - 1 - LONGEST_FISH_LENGTH
    TOP_EDGE = 0
    BOTTOM_EDGE = HEIGHT - 2

    def __init__(self, num_fish, num_kelp, num_bubbler):
        self.fishes = []
        self.bubblers = []
        self.bubbles = []
        self.kelps = []
        self.step = []
        bg('black')
        clear()
        if is_positive_int(num_fish):
            self.num_fish = int(num_fish)
        else:
            raise Exception(
                'Number of fish must be greater than or equal to zero.'
            )

        if is_positive_int(num_kelp):
            self.num_kelp = int(num_kelp)
        else:
            raise Exception(
                'Number of kelp must be greater than or equal to zero.'
            )
        
        if is_positive_int(num_bubbler):
            self.num_bubbler = int(num_bubbler)
        else:
            raise Exception(
                'Number of bubblers must be greater than or equal to zero.'
            )

        for _ in range(self.num_fish):
            self.fishes.append(self.generate_fish())
        
        for _ in range(self.num_bubbler):
            self.bubbler.append(randint(self.LEFT_EDGE, self.RIGHT_EDGE))
        
        for _ in range(self.num_kelp):
            kelp_x = randint(self.LEFT_EDGE, self.RIGHT_EDGE)
            kelp = {
                'x': kelp_x,
                'segments': []
            }
            for _ in range(randint(6, self.HEIGHT - 1)):
                kelp['segments'].append(choice(['(', ')']))
            self.kelps.append(kelp)
        
        self.step = 0

    def display_intro():
        print('-------------------------------------------------------------')
        print('--------------------------Fish Tank--------------------------')
        print('-------------------------------------------------------------')
        print('A peaceful animation of a fish tank. Press CTRL-C to stop.')
        print()

    def main(self):
        self.step = 1
        while True:
            self.simulate_aquarium()
            self.draw_aquarium()
            sleep(1 / self.FRAMES_PER_SECOND)
            self.clear_aquarium()
            self.step += 1
    
    def generate_fish(self):
        fish_type = choice(self.FISH_TYPES)

        color_pattern = choice(('random', 'head-tail', 'single'))
        fish_length = len(fish_type['right'][0])
        if color_pattern == 'random':
            colors = []
            for _ in range(fish_length):
                colors.append(get_random_color())
        if color_pattern == 'single' or color_pattern == 'head-tail':
            colors = [get_random_color()] * fish_length
        if color_pattern == 'head-tail':
            head_tail_color = get_random_color()
            colors[0] = head_tail_color
            colors[-1] = head_tail_color

        fish = {
            'right':                fish_type['right'],
            'left':                 fish_type['left'],
            'colors':               colors,
            'h_speed':              randint(1, 6),
            'v_speed':              randint(5, 15),
            'time_to_h_dir_change': randint(10, 60),
            'time_to_v_dir_change': randint(2, 20),
            'going_right':          choice([True, False]),
            'going_down':           choice([True, False])
        }

        fish['x'] = randint(0, self.WIDTH - 1 - self.LONGEST_FISH_LENGTH)
        fish['y'] = randint(0, self.HEIGHT - 2)
        return fish

    def simulate_aquarium(self):
        pass
    
    def draw_aquarium(self):
        pass

    def clear_aquarium(self):
        pass


def get_random_color(self):
    return choice((
        'black', 'red', 'green', 'yellow', 'blue', 'purple', 
        'cyan', 'white'
    ))

def is_positive_int(num):
    try:
        num = int(num)
        if num < 0 or num % 1 != 0:
            return False
        return True
    except:
        return False