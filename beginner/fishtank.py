from sys import exit, stdout
from random import choice, randint
from time import sleep

try:
    from bext import clear, size, bg, fg, goto
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
        for fish in self.fishes:
            if self.step % fish['h_speed'] == 0:
                if fish['going_right']:
                    if fish['x'] != self.RIGHT_EDGE:
                        fish['x'] += 1
                    else:
                        fish['going_right'] = False
                        fish['colors'].reverse()
                else:
                    if fish['x'] != self.LEFT_EDGE:
                        fish['x'] -= 1
                    else:
                        fish['going_right'] = True
                        fish['colors'].reverse()

            fish['time_to_h_dir_change'] -= 1
            if fish['time_to_h_dir_change'] == 0:
                fish['time_to_h_dir_change'] = randint(10, 60)
                fish['going_right'] = not fish['going_right']
            
            if self.step % fish['v_speed'] == 0:
                if fish['going_down']:
                    if fish['y'] != self.BOTTOM_EDGE:
                        fish['y'] += 1
                    else:
                        fish['going_down'] = False
                else:
                    if fish['y'] != self.TOP_EDGE:
                        fish['y'] -= 1
                    else:
                        fish['going_down'] = True
            
            fish['time_to_v_dir_change'] -= 1
            if fish['time_to_v_dir_change'] == 0:
                fish['time_to_v_dir_change'] = randint(2, 20)
                fish['going_down'] = not fish['going_down']

        for bubbler in self.bubblers:
            if randint(1, 5) == 1:
                self.bubbles.append(
                    {
                        'x': bubbler,
                        'y': self.HEIGHT - 2
                    }
                )
        for bubble in self.bubbles:
            dice_roll = randint(1, 6)
            if dice_roll == 1 and bubble['x'] != self.LEFT_EDGE:
                bubble['x'] -= 1
            elif dice_roll == 2 and bubble['y'] != self.RIGHT_EDGE:
                bubble['x'] += 1
            
            bubble['y'] -= 1
        
        for i in range(len(self.bubbles) - 1, -1 , -1):
            if self.bubbles[i]['y'] == self.TOP_EDGE:
                del self.bubbles[i]
        
        for kelp in self.kelps:
            for i, kelp_segment in enumerate(kelp['segments']):
                if randint(1, 20) == 1:
                    if kelp_segment == '(':
                        kelp['segments'][i] = ')'
                    elif kelp_segment == ')':
                        kelp['segments'][i] = '('
    
    def draw_aquarium(self):
        fg('white')
        goto(0, 0)
        print('Fish Tank    CTRL-C to quit.', end='')

        fg('white')
        for bubble in self.bubbles:
            goto(bubble['x'], bubble['y'])
            print(choice(('o', 'O')), end='')
        
        for fish in self.fishes:
            if fish['going_right']:
                fish_text = \
                    fish['right'][self.step % len(fish['right'])]
            else:
                fish_text = \
                    fish['left'][self.step % len(fish['left'])]
            
            for i, fish_part in enumerate(fish_text):
                fg(fish['colors'][i])
                print(fish_part, end='')
        
        fg('green')
        for kelp in self.kelps:
            for i, kelp_segment in kelp:
                if kelp_segment == '(':
                    goto(kelp['x'], self.BOTTOM_EDGE - i)
                elif kelp_segment == ')':
                    goto(kelp['x'] + 1, self.BOTTOM_EDGE - i)
                print(kelp_segment, end='')
        
        fg('yellow')
        goto(0, self.HEIGHT - 1)
        print(chr(9617) * (self.WIDTH - 1), end='')

        stdout.flush()
                

    def clear_aquarium(self):
        pass


def get_random_color():
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