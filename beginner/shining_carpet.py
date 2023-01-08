class TiledPattern:
    CARPET_TILE = r'''
_ \ \ \_/ __
 \ \ \___/ _
\ \ \_____/ 
/ / / ___ \_
_/ / / _ \__
__/ / / \___
'''

    def __init__(s, num_horizontal_tiles, num_vertical_tiles):
        s.num_horizontal_tiles = num_horizontal_tiles
        s.num_vertical_tiles = num_vertical_tiles
    
