from random import randint
from time import sleep

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