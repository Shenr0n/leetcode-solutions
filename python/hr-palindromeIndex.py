#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'palindromeIndex' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def palindromeIndex(s):
    # Write your code here
    """indexVal = -1
    if len(s) == 1:
        return indexVal
    left = 0
    right = len(s)-1

    while left <= right:
        if s[left]!=s[right]:
            if s[left+1] == s[right]:
                indexVal = left
                left += 1
            else:
                indexVal = right
                right -= 1
        else:
            left += 1
            right -= 1
    return indexVal"""
    n = len(s)
    for i in range(n//2+1):
        if s[i] != s[n-1-i]:
            if s[i] == s[n-2-i] and s[i+1] == s[n-3-i]:
                return n-1-i
            else:
                return i
    return -1
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        fptr.write(str(result) + '\n')

    fptr.close()
