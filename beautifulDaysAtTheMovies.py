#!/bin/python3

import math
import os
import random
import re
import sys

def revDiff(n):
    return n - int(str(n)[::-1])

# Complete the beautifulDays function below.
def beautifulDays(i, j, k):
    tally = 0
    for n in range(i,j+1):
        if revDiff(n) % k == 0:
            tally += 1
    return tally

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ijk = input().split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()
