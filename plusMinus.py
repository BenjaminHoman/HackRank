#!/bin/python

import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))

positiveAmnt, negativeAmnt, zeroAmnt = 0.0, 0.0, 0.0

for number in arr:
    if number > 0:
        positiveAmnt += 1
    elif number < 0:
        negativeAmnt += 1
    else:
        zeroAmnt += 1
        
print positiveAmnt / n
print negativeAmnt / n
print zeroAmnt / n