#!/usr/bin/python

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
#    print "S Length: " + str(len(s))
    if (len(s) < 1) or (len(s) > 100):
        return 0
    elif n < 1 or n > 10**12:
        return 0

    whole = n/len(s)
    remain = n%len(s)

#    print("Whole: " + str(whole) + " Rem: " + str(remain))

    sum = s.count("a") * whole
    sum += s.count("a", 0, remain)

    return sum

if __name__ == '__main__':
#    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = raw_input()

    n = int(raw_input())

    result = repeatedString(s, n)

    print(result)
