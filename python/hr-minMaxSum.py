#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    
    # Write your code here
    arr.sort()
    totalVal = 0
    totalVal = sum(arr)
    print(f'{totalVal-arr[4]} {totalVal-arr[0]}')
        

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
