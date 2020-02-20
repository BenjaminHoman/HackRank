#!/bin/python3

import math
import os
import random
import re
import sys

def split(s):
    mid = len(s) // 2
    off = 0
    if len(s) % 2 != 0:
        off = 1
    return s[:mid], s[mid+off:]

# Complete the theLoveLetterMystery function below.
def theLoveLetterMystery(s):
    half1, half2 = split(s)
    return sum([abs(ord(a) - ord(b)) for a, b in list(zip(half1, half2[::-1]))])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = theLoveLetterMystery(s)

        fptr.write(str(result) + '\n')

    fptr.close()
