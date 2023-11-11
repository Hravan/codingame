# Your mission is to program the device so that it indicates the location of the
# next window Batman should jump to in order to reach the bombs' room as soon as possible.

# Buildings are represented as a rectangular array of windows, the window in the
# top left corner of the building is at index (0,0).

def jump_device(w, h):
    '''Consume width and height of the building and return a function to move
       through a building of the given size
    '''
    min_w = 0
    min_h = 0
    max_w = w - 1
    max_h = h - 1


    def jump(drt, bat_pos):
        '''
        str int int tuple(int, int) -> tuple(int, int)

        Consume a direction of the bomb, with and height of the building and current
        batman position and return coordinates of the place of the building where Batman
        should jump to.
        '''
        #return (0, 0) # stub
        nonlocal min_w, min_h, max_h, max_w

        new_bat_x = bat_pos[0]
        new_bat_y = bat_pos[1]

        if 'U' in drt:
            max_h = bat_pos[1] - 1
            new_bat_y = (max_h + min_h) // 2

        if 'R' in drt:
            min_w = bat_pos[0] + 1
            new_bat_x = (max_w + min_w) // 2

        if 'D' in drt:
            min_h = bat_pos[1] + 1
            new_bat_y = (max_h + min_h) // 2

        if 'L' in drt:
            max_w = bat_pos[0] - 1
            new_bat_x = (max_w + min_w) // 2

        return new_bat_x, new_bat_y

    return jump
