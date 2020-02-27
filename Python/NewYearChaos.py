#!/usr/bin/python

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(final_queue):
    is_invalid     = 0
    arr_len        = len(final_queue)
    answer         = 0
    original_order = range(arr_len + 1)
    queue_order    = range(arr_len + 1)

    # Iterate through the array backwards and see if we can reverse the array back to starting order
    for i in range(arr_len, -1, -1)
        if is_invalid:
            break

        # Know what we are looking for
        # Since we are iterating the array in reverse, our 0 based i + 1 is the position value that should be
        # in this spot. This is what we will test against
        should_be_num = i + 1

        # Get the starting position of final_queue[i]
        is_num = final_queue[i]

        # compare actual spot number to what it should be until you find how many bribes would have happened
        while is_num != should_be_num:
            answer = answer + 1

if __name__ == '__main__':
    t = int(raw_input())

    for t_itr in xrange(t):
        n = int(raw_input())

        q = map(int, raw_input().rstrip().split())

        minimumBribes(q)
