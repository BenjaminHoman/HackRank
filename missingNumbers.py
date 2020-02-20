#!/bin/python3

import math
import os
import random
import re
import sys

def tally(arr):
    t = {}
    for e in arr:
        if e not in t:
            t[e] = 1
        else:
            t[e] += 1
    return t

# Complete the missingNumbers function below.
def missingNumbers(arr, brr):
    tallyA = tally(arr)
    tallyB = tally(brr)
    numbers = []
    for n in set(arr + brr):
        if n in tallyA and n not in tallyB:
            numbers.append(n)
        elif n not in tallyA and n in tallyB:
            numbers.append(n)
        elif n in tallyA and n in tallyB:
            if tallyA[n] != tallyB[n]:
                numbers.append(n)
    print(tallyA)
    print(tallyB)
    return numbers

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    m = int(input())

    brr = list(map(int, input().rstrip().split()))

    result = missingNumbers(arr, brr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
