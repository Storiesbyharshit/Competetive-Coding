#User function Template for python3

def reverseInGroups(A,N,K):
    i=0
    
    # for all elements
    while(i<N):
        '''
        There can be two conditions
        When we have k elements from our current position
        When k elements from current elements don't exist. In such case just reverse the remaining elements
        '''
        # check if first k elements are reversed
        if (i+K<N):
            A[i:i+K]=reversed(A[i:i+K])
            
            i+=K
            
            
        else:
            A[i:]=reversed(A[i:])
            i+=K
    
    return A
