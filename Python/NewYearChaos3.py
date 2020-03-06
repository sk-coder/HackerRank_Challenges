#!/usr/bin/python

import math
import os
import random
import re
import sys


def minimumBribes(arr):
    is_invalid = 0
    arr_len    = len(arr)
    bribes     = 0

    if arr_len >= 10**5:
        is_invalid = 1

    # Iterate through the array backwards and see if we can reverse the array back to starting order
    for i in range(arr_len - 1, -1, -1):
        if is_invalid:
            break

        # Arrays are 0 based, the queue is 1 based,  i + 1 gives us the queue value
        idx = i + 1

        # See if a bribe happened
        if arr[i] != idx:
            # Someone can only bribe forward a max of 2 spaces, test for 1 and 2 bribes
            if arr[i-1] == idx:
                # swap these values and count 1 bribe
                arr[i-1], arr[i] = arr[i], arr[i-1]
                bribes += 1
            elif arr[i-2] == idx:
                arr[i-2], arr[i-1], arr[i] = arr[i-1], arr[i], arr[i-2]
                bribes += 2
            else:
                is_invalid = 1

    if is_invalid:
        print "Too chaotic"
    else:
        print str(bribes)

if __name__ == '__main__':
    f = open("NY_Chaos_TC06.txt", "r")
    line = f.readline()
    t = int(line)

    for t_itr in xrange(t):
        line = f.readline()
        n = int(line)

        line = f.readline()
        q = map(int, line.rstrip().split())

        print""
        minimumBribes(q)
