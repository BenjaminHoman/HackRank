#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    n,k = raw_input().strip().split(' ')
    n,k = [int(n),int(k)]
    a = map(int,raw_input().strip().split(' '))
    
    onTimeStudents = 0
    for arrivalTime in a:
        if arrivalTime <= 0:
            onTimeStudents += 1
    
    if onTimeStudents < k:
        print "YES"
    else:
        print "NO"
