#!/usr/bin/python

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(queue):
    is_invalid     = 0
    arr_len        = len(queue) - 1
    answer         = 0

    # Iterate through the array backwards and see if we can reverse the array back to starting order
    for i in range(arr_len, -1, -1):
        if is_invalid:
            break

        # Know what we are looking for
        # Since we are iterating the array in reverse, our 0 based i + 1 is the position value that should be
        # in this spot. This is what we will test against
        should_be_num = i + 1

        # Get the starting position of final_queue[i]
        is_num = queue[i]

        # Reset the bribe count for 'too complex'
        bribes = 0

        # compare actual spot number to what it should be until you find how many bribes would have happened
        while is_num != should_be_num:
            answer = answer + 1

            # Get the index of the target value
            target_idx = queue.index(should_be_num)

            # Test that the target index isn't more than 2 positions away
            if target_idx < (i - 2):
                is_invalid = 1
                break

            # Swap this value with the next higher index item
            queue[target_idx], queue[target_idx + 1] = queue[target_idx + 1], queue[target_idx]

            # Increment the bribe count
            bribes = bribes + 1

            # Get the value for the i position in the queue for verification
            is_num = queue[i]

    if is_invalid:
        print "Too chaotic"
    else:
        print str(answer)

if __name__ == '__main__':
    t = int(raw_input())

    for t_itr in xrange(t):
        n = int(raw_input())

        q = map(int, raw_input().rstrip().split())

        minimumBribes(q)
