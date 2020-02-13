#!/usr/bin/python

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):
    result = ""

    print len(a)
    for x in range(len(a)):
        print str(a[x]),
    print "\n"

    print "array: " + str(a)
    print "shift: " + str(d)

    if len(a) > 10**6 or len(a) == 0:
        return result
    elif d >= len(a) or d == 0:
        return result

    print str(a[d:])
    print str(a[0:d])

    arr = a[d:]
    arr += a[0:d]

    result = arr

    return result

if __name__ == '__main__':

    nd = raw_input("count & shift: ").split()

    n = int(nd[0])

    d = int(nd[1])

    a = map(int, raw_input("list of chars: ").rstrip().split())

    result = rotLeft(a, d)
    print(' '.join(map(str, result)))
