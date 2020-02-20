#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the balancedSums function below.
def balancedSums(arr):
    total = sum(arr)
    left = 0
    right = total
    print("total " + str(right))
    for i in arr:
        print("left %s, right %s, i %s" % (left, right-i, i))
        if left == right-i:
            return "YES"
        left += i
        right -= i
    return "NO"
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = balancedSums(arr)

        fptr.write(result + '\n')

    fptr.close()
