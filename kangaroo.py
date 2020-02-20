#!/bin/python

import sys

def getIntersection(x1, v1, x2, v2):
    x = x1 - x2
    v = v1 - v2
    if v == 0.0:
        return -1
    intersection = -x/float(v)
    return intersection if intersection >= 0.0 and intersection.is_integer() else -1

def kangaroo(x1, v1, x2, v2):
    return "YES" if getIntersection(x1, v1, x2, v2) >= 0.0 else "NO"

x1, v1, x2, v2 = raw_input().strip().split(' ')
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]
result = kangaroo(x1, v1, x2, v2)
print(result)