def maxOccured(L,R,N,maxx):
    arr = [0] * (maxx + 2)
    for i in range(N):
        arr[L[i]] += 1
        arr[R[i] + 1] -= 1
    for i in range(1, len(arr)):
        arr[i] += arr[i-1]
    maxi = max(arr)
    for i in range(len(arr)):
        if arr[i] == maxi:
            return i
            break
        
