from sys import exit

def invalid_board(reason):
    print(reason)
    return False

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
        if(len(key) != 2):
            return invalid_board("Invalid position")
        num, letter = list(key)
        if(not isNum(num)):
            return invalid_board("Invalid position")
        else:
            num = int(num)
            if(num < 1 or num > 8):
                return invalid_board("Invalid position")
            else:
                pass
        
        if(letter < 'a' or letter >'h'):
            return invalid_board("Invalid position")
        
        if(len(value) == 0):
            return invalid_board("Invalid piece")
        else:
            color = value[:1]
            piece = value[1:]
            if(keyExists(piece_to_dict_map, piece)):
                if(piece_to_dict_map[piece][color] > 0):
                    piece_to_dict_map[piece][color]-=1
                else:
                    return invalid_board("Invalid number of pieces")
            else:
                return invalid_board("Invalid piece")
    return True

# print(isValidChessboard( dict({'1h': 'bking', '1h': 'wqueen',
# '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'})))

def display_inventory(inventory):
    item_total = 0
    result = "Inventory:\n"
    for key, value in inventory.items():
        item_total += int(value)
        result += "%s %s\n" % (value, key)
    result += "Total number of items: %s\n" % (str(item_total))
    return result

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
print(display_inventory(stuff))

# inventory is a dictionary and added_items in a list
def addToInventory(inventory, added_items):
    for item in added_items:
        if(keyExists(inventory, item)):
            inventory[item] += 1
        else:
            inventory[item] = 1
    return inventory

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
print(display_inventory(inv))