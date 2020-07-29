import math
import os
import random
import re
import sys

# Complete the countSwaps function below.
def countSwaps(a):
    swapCounter = 0
    for i in range(len(a)):
        for j in range(len(a)-1):
            if(a[j]>a[j+1]):
                a[j],a[j+1] = a[j+1],a[j]
                swapCounter += 1
    print(f"Array is sorted in {swapCounter} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[-1]}")
            

if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
