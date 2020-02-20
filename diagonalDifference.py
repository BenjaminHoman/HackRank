#!/bin/python

import sys

def sumDiagMatrix(matrix, n, start, incr):
    s = 0
    for i in range(n):
        s += matrix[start[0]][start[1]]
        start[0] += incr[0]
        start[1] += incr[1]
    return s


n = int(raw_input().strip())
a = []
for a_i in xrange(n):
   a_temp = map(int,raw_input().strip().split(' '))
   a.append(a_temp)

x = sumDiagMatrix(a, n, [0,0], [1,1])
y = sumDiagMatrix(a, n, [n-1,0], [-1,1])
print abs(x - y)