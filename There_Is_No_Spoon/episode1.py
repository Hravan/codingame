def find_neighbours(width, height, grid):
    '''int int str -> str
       Consume width and height of a grid and the grid and yield nodes with their
       neighbours.'''
    for j in range(height):
        for i in range(width):
            if grid[j][i] == '.':
                continue
            else:
                for k in range(i + 1, width):
                    if grid[j][k] == '0':
                        right_neigh = ' {} {}'.format(k, j)
                        break
                else:
                    right_neigh = ' -1 -1'

                for k in range(j + 1, height):
                    if grid[k][i] == '0':
                        lower_neigh = ' {} {}'.format(i, k)
                        break
                else:
                    lower_neigh = ' -1 -1'
            yield str(i) + ' ' + str(j) + right_neigh + lower_neigh

def main():
    width = int(input())
    height = int(input())
    grid = [input() for _ in range(height)]
    fn = find_neighbours(width, height, grid)
    for node in fn:
        print(node)
