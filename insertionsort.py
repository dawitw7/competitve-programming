

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    carrier = arr[n-1]
    for i in range(n-1,0,-1):
        if carrier < arr[i-1]:
            arr[i]=arr[i-1]
            print(*arr)
        elif carrier >= arr[i-1]:
            arr[i] = carrier
            print(*arr)
            break
        if i==1 and arr[i-1]>carrier:
            arr[i-1] = carrier
            print(*arr)
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
