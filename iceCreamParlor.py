#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations

def comb_indices(arr, n):
    return list((i,j) for ((i,_),(j,_)) in combinations(enumerate(arr), n))

# Complete the icecreamParlor function below.
def icecreamParlor(m, arr):
    for comb in comb_indices(arr, 2):
        if arr[comb[0]] + arr[comb[1]] == m:
            return [comb[0]+1, comb[1]+1]
    return []

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        m = int(input())

        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = icecreamParlor(m, arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
