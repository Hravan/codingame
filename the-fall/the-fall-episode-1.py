DOWN_OUT_ROOMS = {1, 3, 7, 8, 9, 12, 13}
RIGHT_OUT_ROOMS = {11}
LEFT_OUT_ROOMS = {10}
HORIZONTAL_ROOMS = {2, 6}


def next_room(origin: str, current_room_type: int, position_x: int, position_y: int):
    if current_room_type in DOWN_OUT_ROOMS:
        return position_x, position_y + 1

    if origin == 'TOP':
        if current_room_type in RIGHT_OUT_ROOMS | {5}:
            return position_x + 1, position_y
        elif current_room_type in LEFT_OUT_ROOMS | {4}:
            return position_x - 1, position_y

    if origin == 'LEFT':
        if current_room_type in HORIZONTAL_ROOMS:
            return position_x + 1, position_y
        return position_x, position_y + 1

    if origin == 'RIGHT':
        if current_room_type in HORIZONTAL_ROOMS:
            return position_x - 1, position_y
        return position_x, position_y + 1

    raise ValueError('Not possible to infer the next position.')


# w: number of columns.
# h: number of rows.
w, h = [int(i) for i in input().split()]
rooms = []
for i in range(h):
    rooms.append([])
    line = input()  # represents a line in the grid and contains W integers. Each integer represents one room of a given type.
    rooms[-1].extend(int(room_type) for room_type in line.split())
ex = int(input())  # the coordinate along the X axis of the exit (not useful for this first mission, but must be read).

while True:
    inputs = input().split()
    xi = int(inputs[0])
    yi = int(inputs[1])
    pos = inputs[2]
    next_x, next_y = next_room(pos, rooms[yi][xi], xi, yi)

    print(next_x, next_y)