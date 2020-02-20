#!/bin/python

import sys

def nextMultiple(n, m):
    return n + m - (n % m)

def solve(grades):
    final_grades = []
    for grade in grades:
        if grade < 38:
            final_grades.append(grade)
        elif nextMultiple(grade, 5) - grade < 3:
            final_grades.append(nextMultiple(grade, 5))
        else:
            final_grades.append(grade)
    return final_grades

n = int(raw_input().strip())
grades = []
grades_i = 0
for grades_i in xrange(n):
    grades_t = int(raw_input().strip())
    grades.append(grades_t)
result = solve(grades)
print "\n".join(map(str, result))