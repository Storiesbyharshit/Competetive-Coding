"""

Create an array of N length where ith value will be the last valule for a subsequence of length (i+1).

Iterate over the array, use binary search to find best indexes to place new elements in the dp array.

Longest Increasing Subsequence 
Given an array of integers, find the length of the longest (strictly) increasing subsequence from the given array.

"""

#Python 3

def binarySearch(lst, l, h, value):
    # this function finds the position of the first integer
    # in arr which is greater than or equal to 'value'
    
    if value > lst[h]:
        return h+1
    # if new value is greater than all array values,
    # then it is places at the end
    
    while h>l:
        middle = (h+l)//2
        
        if lst[middle] == value:
            return middle
        
        if lst[middle] > value:
            h = middle
        
        else:
            l = middle + 1
    
    return h

def longestSubsequence(a,n):
    tail = [0 for _ in range(n)]
    tail[0] = a[0]
    # tail[i] holds the last value in a sub sequence of length = i+1
    
    lastIndex = 0 # the position of last filled index in tail[]
    
    for i in range(1,n):
        index = binarySearch( tail, 0, lastIndex, a[i] )
        # getting the furthest possible index for a[i]
        
        tail[index] = a[i]
        lastIndex = max( lastIndex, index )
    
    return lastIndex+1
