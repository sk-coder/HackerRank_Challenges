#!/usr/bin/python

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(arr):
    is_invalid = 0
    arr_len    = len(arr)
    pos_queue  = 0
    val_queue  = 0
    bribes     = 0

    # Iterate through the array to see how many moves needed to be made
    for i in range(arr_len):
        pos = i + 1
        val = arr[i]

        if is_invalid:
            break

        # Is the current value greater than the maximum position shift of 2
        #  this is a fatal flaw
        if val > pos + 2:
            is_invalid = 1
            break

        # Check the status of our Queues
        if pos_queue + val_queue == 0:
            # There is nothing in the queues. Begin checking for numbers that don't match
            if pos != val:
                # we found a discontinuity
                ## save the pos and val into their queues
                pos_queue = pos
                val_queue = val
                ## count the bribe
                bribes = bribes + 1

        # There is an existing discontinuity
        else:
            if pos == val:
                # There is an unchanged position in the queue while discord exists
                # We count this as 2
                bribes = bribes + 2
            else:
                # the numbers don't match. See if it resolves any existing values in the queues
                if pos_queue == val and val_queue == pos:
                    # We have resolved this swap. No additional counts. Clear the queues
                    pos_queue = 0
                    val_queue = 0
                else:
                    bribes = bribes + 1
                    if pos_queue == val:
                        # We found a match for the position in the value. Increase the count and reset the queue.
                        pos_queue = pos
                    elif val_queue == pos:
                        # We found a match for the value in the position
                        val_queue = val


    # Output the result
    if is_invalid:
        print "Too chaotic"
    else:
        print(bribes)


if __name__ == '__main__':
    t = int(raw_input())

    for t_itr in xrange(t):
        n = int(raw_input())

        q = map(int, raw_input().rstrip().split())

        print""
        minimumBribes(q)
