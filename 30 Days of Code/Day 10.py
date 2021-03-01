#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    bin_n = bin(n).replace("0b", "") 
    bin_list = list(bin_n)
    

    count = 0
    temp = 0
    total = 0

    for i in range(0,len(bin_list)):
        if (bin_list[i] == '1'):
            count += 1
        else:
            if (temp < count):
                temp = count
                total = temp
                count = 0
            else:
                total = temp
                count = 0            

    
    if (temp < count):
        temp = count
        total = temp
        count = 0
    else:
        total = temp
        count = 0    

    print (total)
