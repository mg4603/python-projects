class TiledPattern:
    CARPET_TILE = r'''
_ \ \ \_/ __
 \ \ \___/ _
\ \ \_____/ 
/ / / ___ \_
_/ / / _ \__
__/ / / \___
'''

    BRICK_WALL_TILE = r'''
___|___|
_|___|__
'''

    def __init__(s, num_horizontal_tiles, num_vertical_tiles, tile_type):
        s.num_horizontal_tiles = num_horizontal_tiles
        s.num_vertical_tiles = num_vertical_tiles
        s.tile_type = tile_type

    def draw_pattern(s):
        if s.tile_type == 'carpet':
            tile = s.CARPET_TILE
        elif s.tile_type == 'brick wall':
            tile = s.BRICK_WALL_TILE
        elif s.tile_type == 'parenthesis':
            tile = s.PARENTHESIS_TILE
        elif s.tile_type == 'double_hexagon':
            tile = s.DOUBLE_HEXAGON_TILE
        elif s.tile_type == 'robot':
            tile = s.ROBOT
        elif s.tile_type == 'irregular':
            tile = s.IRREGULAR

        for i in range(s.num_vertical_tiles):
            for line in range(tile.strip().splitlines()):
                print(line * s.num_horizontal_tiles)