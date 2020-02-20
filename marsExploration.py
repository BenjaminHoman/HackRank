#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the marsExploration function below.
def marsExploration(s):
    message = ["S", "O", "S"]
    tally = 0
    for i, val in enumerate(s):
        if val != message[i % len(message)]:
            tally += 1
    return tally

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
