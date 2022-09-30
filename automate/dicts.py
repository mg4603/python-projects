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

def isValidChessboard(board):
    board_nums = ['1', '2', '3', '4', '5', '6', '7', '8']
    board_alphs = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    pieces =["pawn", "queen", "bishop", "king", "rook", "knight"]
    colors = ["w", "b"]
    if(type(board) != dict):
        invalid_board("Board has to be a dict of positions and pieces")
    for key, value in board.items():
        if(len(key) > 2):
            invalid_board("Invalid position")
        num, letter = key.split("")
        if()