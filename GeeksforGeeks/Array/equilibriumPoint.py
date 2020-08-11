def equilibriumPoint(A, N):

    # sum of all array elements
    sum = 0
    for i in range(0, N):
        sum += A[i]

    # sum2 is used to store 
    # prefix sum
    sum2 = 0

    for i in range(0, N, +1):
        
        # Update suffix sum
        sum -= A[i]
        
        # If prefix and suffix sums
        # match
        if sum2 == sum:
            return (i + 1)
        
        # Update prefix sum    
        sum2 += A[i]
        
    return -1
        
