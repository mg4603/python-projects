from time import sleep
from math import cos, sin
from sys import platform, exit
from os import system
'''
  0---1
 /|  /|
2---3 |
| 4-|-5
|/  |/
6---7
'''
CUBE_POINT_0 = [-1, -1, -1]
CUBE_POINT_1 = [ 1, -1, -1]


class RotatingPolyhedron:
    PAUSE_AMOUNT = 0.1

    WIDTH = 80
    HEIGHT = 24

    SCALE_X = (WIDTH - 4) // 8
    SCALE_Y = (HEIGHT - 4) // 8
    SCALE_Y *= 2
    
    TRANSLATE_X = (WIDTH - 4) // 2
    TRANSLATE_Y = (HEIGHT - 4) // 2

    LINE_CHAR = '*'

    X_ROTATE_SPEED = 0.03
    Y_ROTATE_SPEED = 0.08
    Z_ROTATE_SPEED = 0.13

    X = 0
    Y = 1
    Z = 2

    def __init__(s):
        pass

    def line(s, x1, y1, x2, y2):
        points = []
        if (x1 == x2  and y1 == y2 + 1) or (y1 == y2 and x1 == x2 + 1):
            return [(x1, y1), (x2, y2)]
        
        is_steep = abs(y2 - y1) > abs(x2 - x1)
        if is_steep:
            x1, y1 = y1, x1
            x2, y2 = y2, x2
        is_reversed = x1 > x2

        if is_reversed:
            x1, x2 = x2, x1
            y1, y2 = y2, y1

            delta_x = x2 - x1
            delta_y = abs(y2 - y1)
            extra_y = int(delta_x / 2)
            current_y = y2
            if y1 < y2:
                y_direction = 1
            else:
                y_direction = -1
            
            for current_x in range(x2, x1 - 1, -1):
                if is_steep:
                    points.append((current_y, current_x))
                else:
                    points.append((current_x, current_y))
                extra_y -= delta_y
                if extra_y <= 0:
                    current_y -= y_direction
                    extra_y += delta_x
        else:
            delta_x = x2 - x1
            delta_y = abs(y2 - y1)
            extra_y = int(delta_x / 2)
            current_y = y1
            if y1 < y2:
                y_direction = 1
            else:
                y_direction = -1
            
            for current_x in range(x1, x2 + 1):
                if is_steep:
                    points.append((current_y, current_x))
                else:
                    points.append((current_x, current_y))
                extra_y -= delta_y
                if extra_y < 0:
                    current_y += y_direction
                    extra_y += delta_x

        return points
    
    def rotate_point(s, x, y, z, ax, ay, az):
        rotated_x = x
        rotated_z = (y * cos(ax)) - (z * sin(ax))
        rotated_y = (y * sin(ax)) + (z * cos(ax))
        x, y, z = rotated_x, rotated_y, rotated_z

        rotated_x = (z * sin(ay)) + (x * cos(ay))
        rotated_y = y
        rotated_z = (z * cos(ay)) - (x * sin(ay))
        x, y, z = rotated_x, rotated_y, rotated_z

        rotated_x = (x * cos(az)) - (y * sin(az))
        rotated_y = (x * sin(az)) + (y * cos(az))
        rotated_z = z

        return (rotated_x, rotated_y, rotated_z)
    
    def adjust_point(s, point):
        return (
            int(point[s.X] * s.SCALE_X + s.TRANSLATE_X),
            int(point[s.Y] * s.SCALE_Y + s.TRANSLATE_Y)
        )