#!/bin/python3

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
    unsorted_right = arr[-1]
    i = n - 1
    while i > 0 and arr[i - 1] > unsorted_right:
        arr[i] = arr[i - 1]
        print(*arr)
        i -= 1
    arr[i] = unsorted_right
    print(*arr)


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
