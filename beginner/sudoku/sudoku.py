from sys import exit
from random import choice
from copy import copy
from pathlib import Path

class SudokuGrid:
    def __init__(s, puzzle):
        pass

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


if __name__ == '__main__':
    main()