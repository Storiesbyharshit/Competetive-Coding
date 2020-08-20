##

def maxSumSubarray(arr, n):
    # Code here
    frwd=[0 for i in range(n)]
    brwd=[0 for i in range(n)]
    curmax = arr[0]
    maxsofar = arr[0]
    frwd[0]=curmax
    for i in range(1, n):
        curmax = max(arr[i], curmax + arr[i])
        maxsofar = max(maxsofar, curmax)
        frwd[i] = curmax
    curmax = maxsofar = brwd[n-1] = arr[n-1]
    for i in range(n-2, -1, -1):
        curmax = max(arr[i], curmax + arr[i])
        maxsofar = max(maxsofar, curmax)
        brwd[i]=curmax
    final = maxsofar
    for i in range(1,n-1):
        final = max(final, frwd[i-1]+brwd[i+1])
    return final
    
    
    """
    If element removal condition is not applied, we can solve this problem using Kadane’s algorithm but here one element can be removed also for increasing maximum sum. This condition can be handled using two arrays, forward and backward array, these arrays store the current maximum subarray sum from starting to ith index, and from ith index to ending respectively.
In below code, two loops are written, first one stores maximum current sum in forward direction in fw[] and other loop stores the same in backward direction in bw[]. Getting current maximum and updation is same as Kadane’s algorithm.
Now when both arrays are created, we can use them for one element removal conditions as follows, at each index i, maximum subarray sum after ignoring i’th element will be fw[i-1] + bw[i+1] so we loop for all possible i values and we choose maximum among them.

Total time complexity and space complexity of solution is O(N)"""
