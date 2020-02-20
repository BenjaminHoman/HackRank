#!/bin/python3

import math
import os
import random
import re
import sys

def criteria(last, current):
    return not current.startswith('0') and not last.startswith('0') and (int(current)-int(last)==1)

def shouldIncreaseSplit(current):
    current = int(current)
    return len(str(current + 1)) > len(str(current))

#numbers, isBeautiful
def split(digits, split_amnt):
    numbers, current_number, split_n = [], '', split_amnt
    for digit in digits:
        if len(current_number) >= split_n:
            if len(numbers) and not criteria(numbers[-1], current_number):
                return split(s, split_amnt+1)
            if shouldIncreaseSplit(current_number):
                split_n += 1
            numbers.append(current_number)
            current_number = digit
        else:
            current_number += digit
    if len(current_number):
        numbers.append(current_number)
    return numbers, len(numbers) > 1 and criteria(numbers[-2], numbers[-1])

def is_beautiful(s):
    split_numbers, beautiful = split(s, 1)
    if beautiful:
        print("YES %s" % split_numbers[0])
    else:
        print("NO")

if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        s = input()

        is_beautiful(s)
