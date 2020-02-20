#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    a = sorted(a)
    print(a)
    arrays = []
    for index, n in enumerate(a):
        if index == 0:
            arrays.append([n])
        else:
            if abs(arrays[-1][0] - n) <= 1:
                arrays[-1].append(n)
            else:
                arrays.append([n])
    print(arrays)
    return max(map(lambda a: len(a), arrays))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
