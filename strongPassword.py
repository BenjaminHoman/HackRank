#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumNumber function below.
def minimumNumber(n, password):
    regexes = ['[!@#$%\^&*\(\)\-\+]', '[0-9]', '[a-z]', '[A-Z]']
    missing = 0
    for r in regexes:
        match = re.search(r, password)
        if match == None:
            missing += 1

    return max(6 - len(password), missing)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
