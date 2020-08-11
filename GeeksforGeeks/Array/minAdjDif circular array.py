def minAdjDiff(arr, n):
    
    res = abs(arr[0]-arr[1])#Store difference of arr[0], arr[1]
    
    for i in range (2, n): #Start from 2 till end
        res = min(res, abs(arr[i]-arr[i-1])) #finding min
    
    
    res = min(res, abs(arr[0]-arr[n-1]))  #finally checking last and first element as it's circular
    
    return res
    
