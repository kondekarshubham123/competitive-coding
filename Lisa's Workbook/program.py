#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the workbook function below.
def workbook(n, k, arr):
    specialprob = 0
    EndPageNo = 0

    for i in range(n):
        startPageNo = EndPageNo+1
        EndPageNo += (arr[i] // k + (1 if arr[i]%k else 0))
        check = 0
        for j in range(startPageNo,EndPageNo+1):
            if check + k <= arr[i]:
                check+=k
                specialprob += 1 if j in list(range(check - k+1,check+1)) else 0
            else:
                pre = check
                check+=arr[i]%k
                specialprob += 1 if j in list(range(pre+1,check+1)) else 0
    return specialprob

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = workbook(n, k, arr)
    print(result)

    #fptr.write(str(result) + '\n')

    #fptr.close()
