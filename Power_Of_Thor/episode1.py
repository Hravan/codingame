import math

def direction(p1, p2):
    '''Take coordinates of two points on a screen and return the
       direction from one to another'''
    angle = findAngle(p1, p2)

    drtn = angleToDirection(angle)

    return drtn

def findAngle(p1, p2):
    '''Take two points on a screen and return angle between them'''
    delta_x = p2[0] - p1[0]
    delta_y = -(p2[1] - p1[1])
    angle = math.atan2(delta_y, delta_x)
    return angle

def angleToDirection(angle):
    '''Take an angle in radians and return a direction that represents this angle'''

    if angle <= - 7 * math.pi / 8 or angle > 7 * math.pi / 8:
        return 'W'

    elif angle > 5 * math.pi / 8:
        return 'NW'

    elif angle > 3 * math.pi / 8:
        return 'N'

    elif angle > math.pi / 8:
        return 'NE'

    elif angle > - math.pi / 8:
        return 'E'

    elif angle > - 3 * math.pi / 8:
        return 'SE'

    elif angle > - 5 * math.pi / 8:
        return 'S'

    else:
        return 'SW'

    return ''

def move(drtn, start):
    '''Consume direction and the starting place and return the end of moving
       one step in the given direction.'''
    if drtn == 'N':
        end = start[0], start[1] - 1

    elif drtn == 'S':
        end = start[0], start[1] + 1

    elif drtn == 'E':
        end = start[0] + 1, start[1]

    elif drtn == 'W':
        end = start[0] - 1, start[1]

    elif drtn == 'NE':
        end = start[0] + 1, start[1] - 1

    elif drtn == 'NW':
        end = start[0] - 1, start[1] - 1

    elif drtn == 'SE':
        end = start[0] + 1, start[1] + 1

    else:
        end = start[0] - 1, start[1] + 1

    return end
