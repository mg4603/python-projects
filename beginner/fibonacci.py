class Fibonacci:
    def __init__(self):
        pass
    
    def display_intro(self):
        print('--------------------------------------------------------------')
        print('----------------------Fibonacci Sequence----------------------')
        print('--------------------------------------------------------------')
        print()
        print('The Fibonacci sequence begins with 0 and 1, and the next')
        print('number is the sum of the previous two numbers. The sequence')
        print('continues forever: ')
        print()
        print('{}\n{}\n\n'.format(
                '0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377,',
                '610, 987, 1597...'))