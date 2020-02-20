#!/bin/python3

import math
import os
import random
import re
import sys

def most_frequent(List): 
    dict = {} 
    count, itm = 0, '' 
    for item in reversed(List): 
        dict[item] = dict.get(item, 0) + 1
        if dict[item] >= count : 
            count, itm = dict[item], item 
    return(itm)

def tally(s):
    t = {}
    for c in s:
        if c not in t:
            t[c] = 1
        else:
            t[c] += 1

    return list(map(lambda e: e[1], t.items()))

# Complete the isValid function below.
def isValid(s):
    char_counts = tally(s)
    if len(set(char_counts)) == 1:
        return "YES"

    freq = most_frequent(char_counts)
    char_counts = list(filter(lambda e: e != freq, char_counts))
    print(char_counts)
    if len(char_counts) == 1:
        if char_counts[0] - 1 == freq or char_counts[0] - 1 == 0:
            return "YES"
    return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
