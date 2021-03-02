#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    wordlist = list(s.split(" "))
    
    for i in range(0, len(wordlist)):
        wordlist[i] = wordlist[i].capitalize()
    
    name = " ".join(map(str, wordlist))
    return name
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
