from sys import exit
from random import choice
from copy import copy
from pathlib import Path

class SudokuGrid:
    GRID_LENGTH = 9
    BOX_LENGTH = 3
    EMPTY_SPACE = ' '
    FULL_GRID_SIZE = GRID_LENGTH * GRID_LENGTH
    def __init__(s, puzzle):
        s.original_setup = puzzle.strip()
        s.grid = {}
        s.reset_grid()
        s.moves = []

    def is_solved(s):
        pass

    def display(s):
        pass

    def undo(s):
        pass

    def reset_grid(s):
        pass

    def make_move(s):
        pass

def display_intro():
    print('Sudoku Puzzle')
    print()
    print('Sudoku is a number placement logic puzzle game. A sudoku grid is')
    print('a 9x9 grid of numbers. Try to place numbers in the grid such that')
    print('every row, column and 3x3 box has the numbers 1 through 9 once')
    print('and only once.')
    print()
    print('For example, here is a starting Sudoku grid and its solved form:')
    print()
    print('     5 3 . | . 7 . | . . .       5 3 4 | 6 7 8 | 9 1 2')
    print('     6 . . | 1 9 5 | . . .       6 7 2 | 1 9 5 | 3 4 8')
    print('     . 9 8 | . . . | . 6 .       1 9 8 | 3 4 2 | 5 6 7')
    print('     ------+-------+------       ------+-------+------')
    print('     8 . . | . 6 . | . . 3       8 5 9 | 7 6 1 | 4 3 2')
    print('     4 . . | 8 . 3 | . . 1  -->  4 2 6 | 8 5 3 | 7 9 1')
    print('     7 . . | . 2 . | . . 6       7 1 3 | 9 2 4 | 8 5 6')
    print('     ------+-------+------       ------+-------+------')
    print('     . 6 . | . . . | 2 8 .       9 6 1 | 5 3 7 | 2 8 4')
    print('     . . . | 4 1 9 | . . 5       2 8 7 | 4 1 9 | 6 3 5')
    print('     . . . | . 8 . | . 7 9       3 4 5 | 2 8 6 | 1 7 9')
    print()

def get_command():
    '''
    action: move, or reset, new, undo, original, quit
    move: b4 9
    '''
    print()
    print('Enter a move or RESET, NEW, UNDO, ORIGINAL or QUIT:')
    print('For example, a move looks like "B4 9".)')
    while True:
        command = input('> ').upper()
    
        if command in ('RESET', 'NEW', 'UNDO', 'ORIGINAL', 'QUIT'):
            return command
        
        if len(command.split()) == 2:
            position, number = command.split()
            if len(position) != 2:
                print('Invalid position')
                continue
            
            column, row = position
            if column not in 'ABCDEFGHI':
                print('Column {} is invalid.'.format(column))
                continue

            if row not in '123456789':
                print('Row {} is invalid.'.format(row))
                continue
            
            if number not in '123456789':
                print('Select a number between 1 and 9, not {}'.format(number))
                continue
            return column, row, number 

        print('Invalid input.')
        print('Please try again.')

def main():
    with Path('sudokupuzzles.txt').open('r') as file:
        puzzles = file.readlines()
    
    puzzles = [puzzle.strip() for puzzle in puzzles]

    display_intro()
    input('Press Enter to begin...')

    grid = SudokuGrid(choice(puzzles))

    #main game loop
    while True:
        grid.display()

        if grid.is_solved():
            print('Congratulations! You solved the puzzle.')
            exit('Thanks for playing!')
        
        command = get_command()
        if len(command) > 1:
            column, row, number = command
        
        if command == 'RESET':
            grid.reset_grid()
            continue
        
        if command == 'NEW':
            grid = SudokuGrid(choice(puzzles))
            continue
        
        if command == 'UNDO':
            grid.undo()
            continue
        
        if command == 'ORIGINAL':
            original_grid = SudokuGrid(grid.original_setup)
            print('The original grid looked like this:')
            input('Press Enter to continue...')
            continue

        if command == 'QUIT':
            exit('Thanks for playing!')
        
        if not grid.make_move():
            print('You cannot overwrite the original grid\'s numbers.')
            print('Enter ORIGINAL to view the original grid.')
            input('Press Enter to continue...')
        

if __name__ == '__main__':
    main()