from random import randint
from time import sleep
from sys import exit

class ProgressBar:
    BAR = chr(9608)
    def __init__(s):
        pass
    
    def get_progress_bar(s, progress, total, bar_width=40):
        if progress > total:
            progress = total
        elif progress < 0:
            progress = 0

        progress_bar = '['
        num_of_bars = int(progress / total * bar_width)
        
        progress_bar += s.BAR * num_of_bars
        progress_bar += ' ' * (bar_width - num_of_bars)

        progress_bar += '] {}% {}/{}'.format(
            round(progress / total * 100 , 1),
            progress,
            total
        )
        return progress_bar

    def display_intro(s):
        print('Progress Bar Simulation')
        print()

def get_simulation_type():
        print('Enter type of progress bar to simulate:')
        print('\t1) Progress Bar')
        print('\t2) Rotating wheel')
        print('\t3) Loading bar')
        print('\t4) Quit')
        while True:
            response = input('> ')
            if response.isdecimal():
                response = int(response)
                if 1 <= response <= 4:
                    return response
            print('Please enter an integer between 1 and 4')

def main():
    progress_bar = ProgressBar()
    progress_bar.display_intro()
    simulation_type = get_simulation_type()
    assert 1 <= simulation_type <= 4, 'Invalid simulation type'
    if simulation_type == 1:
        progress_bar_sim(progress_bar)
    elif simulation_type == 2:
        rotating_wheel_sim(progress_bar)
    elif simulation_type == 3:
        loading_bar_sim(progress_bar)
    elif simulation_type == 4:
        exit()
