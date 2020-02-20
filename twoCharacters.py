#!/bin/python3

import math
import os
import random
import re
import sys
from functools import reduce
from itertools import combinations

def is_alternate(s):
    return len(set(s)) == 2 and all([e[0] != e[1] for e in list(zip(s[1:], s))])

# Complete the alternate function below.
def alternate(s):
    alternating = []
    unique = set(s)
    if len(unique) < 2:
        return 0
    for comb in combinations(unique, len(unique) - 2):
        new_s = s
        for c in list(comb):
            new_s = new_s.replace(c, "")
        if is_alternate(new_s):
            alternating.append(new_s)
    ranked = sorted(alternating, key=lambda e: len(e), reverse=True)
    if len(ranked):
        return len(ranked[0])
    return 0

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    s = input()

    result = alternate(s)

    fptr.write(str(result) + '\n')

    fptr.close()
