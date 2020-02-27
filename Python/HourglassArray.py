#!/usr/bin/python

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def hourglassSum(arr):
    if len(arr)  != 6:
        return False
    elif len(arr[0]) != 6:
        return False
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] < -9 or arr[i][j] > 9:
                return False

    high = -9 * 7

    for i in range(0, 4):
        for j in range(0, 4):
            print "I: " + str(i) + " J: " + str(j)
            print "  Row 1: " + str(sum(arr[i][j:j+2]))
            print "  Row 2: " + str(arr[i+1][j+1])
            print "  Row 3: " + str(sum(arr[i+2][j:j+2]))
            val = sum(arr[i][j:j+2])
            val += arr[i+1][j+1]
            val += sum(arr[i+2][j:j+2])
            if val > high:
                high = val

    return high

if __name__ == '__main__':

    for _ in xrange(6):
        arr.append(map(int, raw_input().rstrip().split()))

    result = hourglassSum(arr)

    print(result)
