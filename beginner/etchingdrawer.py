class EtchingDrawer:
    UP_DOWN_CHAR = chr(9474)
    LEFT_RIGHT_CHAR = chr(9472)
    DOWN_RIGHT_CHAR = chr(9484)
    DOWN_LEFT_CHAR = chr(9488)

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