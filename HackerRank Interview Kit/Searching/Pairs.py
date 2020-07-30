import math
import os
import random
import re
import sys

# Complete the pairs function below.
def pairs(k, arr):
    test = set(arr) #just to make fast speed
    count = 0
    for num in test:
        if (num+k)in test:
            count = count+1
    return count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
