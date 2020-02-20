#!/bin/python

import sys

def solve(arr):
    sum_arr = sum(arr)
    min_arr = min(arr)
    max_arr = max(arr)
    return (sum_arr - max_arr, sum_arr - min_arr)

arr = map(int, raw_input().strip().split(' '))
answer = solve(arr)
print answer[0], answer[1]