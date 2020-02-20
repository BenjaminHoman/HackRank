#!/bin/python3

import math
import os
import random
import re
import sys

def getHeight(heights, c):
    return heights[ord(c) - 97]

# Complete the designerPdfViewer function below.
def designerPdfViewer(h, word):
    return max(map(lambda c: getHeight(h, c), word)) * len(word)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
