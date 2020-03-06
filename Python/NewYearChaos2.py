#!/usr/bin/python

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(arr):
    arr_len    = len(arr)
    is_valid   = 1
    bribes     = 0
    in_order   = 1
    idx_sum    = 0
    val_sum    = 0
    last_match = 0

    # Test for a too long array
    if arr_len >= 10**5:
        is_valid = 0

    if is_valid:
        # Continue processing the array

        # Iterate through the array to see how many moves needed to be made
        for i in range(arr_len):
            idx = i + 1
            val = arr[i]

            # Is the current value greater than the maximum position shift of 2
            if val > idx + 2:
                is_valid = 0
                break

            if in_order:
                # did we find a mis-match?
                if idx != val:
                    in_order = 0
                    idx_sum  = idx
                    val_sum  = val

            else:
                # add idx and val to sums, we will use this later
                idx_sum = idx_sum + idx
                val_sum = val_sum + val

                # is the value less than the index
                if val < idx:
                    # This person got bribed. Count how many times
                    bribes = bribes + (idx - val)

                    if last_match > val:
                        bribes = bribes + 1

                    last_match = val

                    if idx_sum == val_sum:
                        # we have found the end of this series of bribes
                        in_order = 1
                        idx_sum  = 0
                        val_sum  = 0

                elif val == idx:
                    # This person had to bribe someone to remain in the same spot
                    bribes = bribes + 1


    # Output the result
    if is_valid:
        print(bribes)
    else:
        print "Too chaotic"


if __name__ == '__main__':
    t = int(raw_input())

    for t_itr in xrange(t):
        n = int(raw_input())

        q = map(int, raw_input().rstrip().split())

        print""
        minimumBribes(q)
