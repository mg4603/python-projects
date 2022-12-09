class EtchingDrawer:
    UP_DOWN_CHAR = chr(9474)
    LEFT_RIGHT_CHAR = chr(9472)
    DOWN_RIGHT_CHAR = chr(9484)
    DOWN_LEFT_CHAR = chr(9488)
    UP_RIGHT_CHAR = chr(9492)
    UP_LEFT_CHAR = chr(9496)
    UP_DOWN_RIGHT_CHAR = chr(9500)
    UP_DOWN_LEFT_CHAR = chr(9508)
    DOWN_LEFT_RIGHT_CHAR = chr(9516)
    UP_LEFT_RIGHT_CHAR = chr(9624)
    CROSS_CHAR = chr(9532)
    def __init__(self):
        pass

    def display_intro(self):
        print('--------------------------------------------------------------')
        print('------------------------Etching Drawer------------------------')
        print('--------------------------------------------------------------')
        print('An art program that draws a continuous line around the screen')
        print('using the WASD keys. Inspired by Etch A Sketch toys.')
        print('')
        print('For example you can draw Hilbert Curve fractal with:')
        print('SDWDDSASDSAAWASSDSASSDWDSDWWAWDDDSASSDWDSDWWAWDWWASAAWDWAWDDSDW')
        print('')

    def main(self):
        pass