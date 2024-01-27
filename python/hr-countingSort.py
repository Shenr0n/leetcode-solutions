#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countingSort(arr):
    
    # maxVal = max(arr)
    
    count = [0] * 100
    
    for num in arr:
        count[num] += 1
    
    '''for i in range(1, maxVal+1):
        count[i] += count[i-1]
    
    result = [0] * (len(arr))
    for num in reversed(arr):
        result[count[num]-1] = num
        count[num] -= 1
    
    return result'''
    return count
        
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
