#!/usr/bin/python

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    i = 0
    hops = 0

    if not (len(c) < 2 or len(c) > 100):
        while i < len(c):
            print "I: " + str(i) + " hops: " + str(hops)
            if i == (len(c) - 1):
                i += 1
            elif i == (len(c) - 2):
                i += 1
                hops += 1
            elif c[(i + 2)] == 0:
                i += 2
                hops += 1
            else:
                i += 1
                hops += 1

    return hops


if __name__ == '__main__':
#    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    c = map(int, raw_input().rstrip().split())

    result = jumpingOnClouds(c)

    print result
#    fptr.write(str(result) + '\n')

#    fptr.close()
