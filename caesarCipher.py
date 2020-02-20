#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the caesarCipher function below.
def caesarCipher(s, k):
    newS = ""
    for c in s:
        if re.search("[a-zA-Z]", c) == None:
            newS += c
        else:
            normal = 0
            if c.isupper():
                normal = 65
            else:
                normal = 97
            newS += chr(((ord(c) - normal + k) % 26) + normal)
    return newS

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    k = int(input())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
