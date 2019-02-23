# Write a program that prints the temperature closest to 0 among input data.
# If two numbers are equally close to zero, positive integer has to be considered
# closest to zero (for instance, if the temperatures are -5 and 5, then display 5).

from functools import reduce

def closestZero(numbers, n):
    '''Consume a list of integers and its number and return the number that is
       closest to 0. In case of a tie return the positive number. If n == 0, return 0'''
    if n == 0:
        return 0

    closest = reduce(closerZero, numbers)

    return closest

def closerZero(n, m):
    '''Consume two numbers and return one that is closer to zero. Return the positive
       one in case of a tie.'''

    if abs(n) == abs(m):
        # if n is not bigger than 0 then either n == m or m > 0, in both cases
        # we can return m
        return n if n > 0 else m
    elif abs(n) < abs(m):
        return n
    else:
        return m
