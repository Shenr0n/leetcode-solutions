#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'flippingMatrix' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#

def flippingMatrix(matrix):
    # Write your code here
    n = int(len(matrix) / 2)
    maxVal = 0
    total = 0
    
    for row in range(0,n):
        for col in range(0,n):
            maxVal = max(matrix[row][col],matrix[row][2*n-col-1],matrix[2*n-row-1][col],matrix[2*n-row-1][2*n-col-1])
        
            total += maxVal
    return total

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        matrix = []

        for _ in range(2 * n):
            matrix.append(list(map(int, input().rstrip().split())))

        result = flippingMatrix(matrix)

        fptr.write(str(result) + '\n')

    fptr.close()
