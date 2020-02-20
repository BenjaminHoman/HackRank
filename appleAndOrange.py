#!/bin/python

import sys

def isOnHouse(x_axis, s, t):
    return x_axis >= s and x_axis <= t

s,t = raw_input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = raw_input().strip().split(' ')
a,b = [int(a),int(b)]
m,n = raw_input().strip().split(' ')
m,n = [int(m),int(n)]
apples = map(int,raw_input().strip().split(' '))
oranges = map(int,raw_input().strip().split(' '))

print sum([1 if isOnHouse(a+apple, s, t) else 0 for apple in apples])
print sum([1 if isOnHouse(b+orange, s, t) else 0 for orange in oranges])
