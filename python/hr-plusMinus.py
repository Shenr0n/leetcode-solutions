#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    lenArr = len(arr)
    posCount = 0
    negCount = 0
    zeroCount = 0
    
    for i in range(0, lenArr):
        if arr[i] == 0:
            zeroCount += 1
        elif arr[i] > 0:
            posCount += 1
        elif arr[i] < 0:
            negCount += 1
    print(round(posCount/lenArr, 6))
    print(round(negCount/lenArr, 6))
    print(round(zeroCount/lenArr, 6))
    
    # Write your code here

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
