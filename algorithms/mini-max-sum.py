# -------------------------------------------------------
# Mini-Max Sum - https://www.hackerrank.com/challenges/mini-max-sum/
# -------------------------------------------------------
# Author: Arshad Mehmood
# Github: https://github.com/arshad115
# Blog: https://arshadmehmood.com
# LinkedIn: https://www.linkedin.com/in/arshadmehmood115
# Date : 2020-07-24
# Project: HackerRank
# -------------------------------------------------------
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    arrs = sorted(arr)

    msum = sum(arrs[:4])
    maxsum = sum(arrs[1:])

    print(f'{msum} {maxsum}')


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
