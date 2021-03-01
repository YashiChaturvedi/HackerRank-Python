#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the factorial function below.
def factorial(n):
    if (n == 1):
        return n
    else:
        fact = n * factorial(n-1)
        return fact

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())
    
    if n==1:
        result = 1
    else: 
        result = factorial(n)
    
    fptr.write(str(result) + '\n')

    fptr.close()