def leaders(A,N):
    ans=[]
    maxx=A[N-1]
    '''
    start traversing the array from last element
    and compare the element with the max element
    on its right. If current element is the maximum
    till now, then current element is also leader
    '''
    for i in range(N-1,-1,-1):
        if A[i]>=maxx:
            maxx=A[i]
            ans.append(maxx)
    ans.reverse()
    return ans
