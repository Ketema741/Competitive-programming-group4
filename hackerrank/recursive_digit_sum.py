#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def superDigit(n, k):
    # If n has only one digit, return it
    if len(n) == 1:
        return int(n)

    # Otherwise, find the sum of the digits of n
    sum_of_digits = sum([int(digit) for digit in n])

    # Multiply the sum by k
    sum_of_digits *= k

    # Call the superDigit function recursively on the sum
    return superDigit(str(sum_of_digits), 1)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
