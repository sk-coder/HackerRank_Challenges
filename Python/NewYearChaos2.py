#!/usr/bin/python

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(arr):
    arr_len    = len(arr)
    is_invalid = 0
    bribes     = 0
    in_order   = 1
    low_idx    = 0
    last_match = 0

    # Iterate through the array to see how many moves needed to be made
    for i in range(arr_len):
        idx = i + 1
        val = arr[i]

        # A little debug code
        print "I: " + str(i) + "  Idx: " + str(idx) + "  Val: " + str(val) + "  Ord: " + str(in_order)

        # Is the current value greater than the maximum position shift of 2
        if val > idx + 2:
            is_invalid = 1
            break

        if in_order:
            # did we find a mis-match?
            if idx != val:
                in_order  = 0
                print " -- Unordered!"

        else:
            # is the value less than the index
            if val < idx:
                # This person got bribed. Count how many times
                bribes = bribes + (idx - val)

                if last_match > val:
                    bribes = bribes + 1

                last_match = val
            elif val == idx:
                # This person had to bribe someone to remain in the same spot
                bribes = bribes + 1
            print "  Br: " + str(bribes) + "  last: " + str(last_match)


    # Output the result
    print "---------------"
    if is_invalid:
        print "Too Chaotic"
    else:
        print(bribes)


if __name__ == '__main__':
    t = int(raw_input())

    for t_itr in xrange(t):
        n = int(raw_input())

        q = map(int, raw_input().rstrip().split())

        print""
        minimumBribes(q)
