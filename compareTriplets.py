#!/bin/python

import sys

def award(tally, a, b):
    return (tally[0] + (1 if a > b else 0), tally[1] + (1 if b > a else 0))

def solve(a0, a1, a2, b0, b1, b2):
    return award(award(award((0, 0), a0, b0), a1, b1), a2, b2)

a0, a1, a2 = raw_input().strip().split(' ')
a0, a1, a2 = [int(a0), int(a1), int(a2)]
b0, b1, b2 = raw_input().strip().split(' ')
b0, b1, b2 = [int(b0), int(b1), int(b2)]
result = solve(a0, a1, a2, b0, b1, b2)
print " ".join(map(str, result))