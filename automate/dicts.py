from ast import excepthandler
import re
from sys import exit

def invalid_board(reason):
    print(reason)
    exit(0)

def isNum(num):
    try:
        int(num)
        return True
    except ValueError:
        return False

def keyExists(dictionary, key):
    try:
        dictionary[key]
        return True
    except KeyError:
        return False


def isValidChessboard(board):
    board_nums = ['1', '2', '3', '4', '5', '6', '7', '8']
    board_alphs = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    pieces =["pawn", "queen", "bishop", "king", "rook", "knight"]
    colors = ["w", "b"]
    if(type(board) != dict):
        invalid_board("Board has to be a dict of positions and pieces")
    pawn = {
            "w":8,
            "b": 8
            }

    bishop = {
            "w":2,
            "b":2
            }

    rook = {
            "w":2,
            "b":2
            }

    knight = {
            "w":2,
            "b":2
            }
    queen = {
            "w":1,
            "b":1
            }

    king = {
            "w":1,
            "b":1
            }

    piece_to_dict_map = {
        "king"  : king,
        "queen" : queen,
        "bishop": bishop,
        "knight": knight,
        "rook"  : rook,
        "pawn"  : pawn
    }

    for key, value in board.items():
        if(len(key) > 2):
            invalid_board("Invalid position")
        num, letter = key.split("")
        if(not isNum(num)):
            invalid_board("Invalid position")
        else:
            num = int(num)
            if(num < 1 or num > 8):
                invalid_board("Invalid position")
            else:
                pass
        
        if(letter < 'a' or letter >'h'):
            invalid_board("Invalid position")
        
        if(len(value) == 0):
            invalid_board("Invalid piece")
        else:
            color = value[:1]
            piece = value[1:]
            if(keyExists(piece_to_dict_map, piece)):
                if(piece_to_dict_map[piece][color] > 0):
                    piece_to_dict_map[piece][color]-=1
                else:
                    invalid_board("Invalid number of pieces")
            else:
                invalid_board("Invalid piece")
    return True