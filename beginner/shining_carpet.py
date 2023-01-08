class TiledPattern:
    CARPET_TILE = r'''_ \ \ \_/ __
 \ \ \___/ _
\ \ \_____/ 
/ / / ___ \_
_/ / / _ \__
__/ / / \___'''

    BRICK_WALL_TILE = r'''___|___|
_|___|__
'''

    PARENTHESIS_TILE = r'''((  )
 ))( '''

    DOUBLE_HEXAGON_TILE = r''' / __ \ \__/ /
/ /  \ \____/ 
\ \__/ / __ \ 
 \____/ /  \ \
'''
    ROBOT_TILE = r'''/ ___ \ ^ 
 /   \ VVV
|() ()|   
 \ ^ / ___
\ VVV /   
)|   |() (
'''
    
    IRREGULAR_TILE = r'''  \__ 
__/  \
  \   
__/   
  \__/
  /   
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
        elif s.tile_type == 'double hexagon':
            tile = s.DOUBLE_HEXAGON_TILE
        elif s.tile_type == 'robot':
            tile = s.ROBOT_TILE
        elif s.tile_type == 'irregular':
            tile = s.IRREGULAR_TILE

        for i in range(s.num_vertical_tiles):
            for line in tile.splitlines():
                print(line * s.num_horizontal_tiles)


def main():
    carpet = TiledPattern(8, 4, 'carpet')
    carpet.draw_pattern()
    print()
    wall = TiledPattern(12, 8, 'brick wall')
    wall.draw_pattern()
    print()
    parenthesis = TiledPattern(19, 8, 'parenthesis')
    parenthesis.draw_pattern()
    print()
    hexagons = TiledPattern(7, 4, 'double hexagon')
    hexagons.draw_pattern()
    print()
    robot = TiledPattern(10, 4, 'robot')
    robot.draw_pattern()
    print()
    irregular = TiledPattern(16, 4, 'irregular')
    irregular.draw_pattern()
    print()
