
import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    # Write your code here
    i= 0
    c = 0
    n=len(a)
    while(i<n):
        j= 0
        while(j<(n-1)):
            if (a[j] > a[j + 1]):
                x = a[j]
                a[j]= a[j+1]
                a[j+1] = x
                c+=1
            j+=1
        i+=1  
    arr = [0,0,0] 
    arr[0] = c
    arr[1]= a[0]
    arr[2]= a[n-1]
    print("Array is sorted in" ,arr[0] ,"swaps.")
    print("First Element:",arr[1])
    print("Last Element:",arr[2])
    return 0
    # Write your code here

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
