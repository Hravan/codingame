# Casablanca’s hippodrome is organizing a new type of horse racing: duals. During a dual, only two horses will participate in the race. In order for the race to be interesting, it is necessary to try to select two horses with similar strength.
# Write a program which, using a given number of strengths, identifies the two closest strengths and shows their difference with an integer (≥ 0).

# INPUT
# Line 1: Number N of horses
# The N following lines: the strength Pi of each horse. Pi is an integer.

# Output
#The difference D between the two closest strengths. D is an integer greater than or equal to 0.

# Constraints
# 1 < N  < 100000
# 0 < Pi ≤ 10000000

from functools import reduce

def find_dual(horses):
    '''Consume a ist of horses strengths and return difference between two closest
       of them.'''
    horses.sort()
    horses_pairs = zip(horses[:-1], horses[1:])
    dual = min(x[1] - x[0] for x in horses_pairs)


    return dual
