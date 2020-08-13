# finding the maximum sum subarray
def kadane(arr):
    
    n=len(arr)
    
    maxend=arr[0]
    maxi=arr[0]
    
    for i in range(1,n):
        maxend=max(maxend+arr[i],arr[i])
        maxi=max(maxi,maxend)
    return maxi
  
# finding the part of the array which is to be excluded
def reverseKadane(arr,num):
    sum=0
    for i in range(0,num):
        sum+=arr[i]
    min_minus=0
    maxi=sum
    for i in range(0,num):
        min_minus=min(min_minus+arr[i], arr[i])
        if min_minus==sum:
            return -999999
        maxi=max(maxi, sum-min_minus)
    
    return maxi
        
def circularSubarraySum(arr,n):
    k=kadane(arr)
    rk=reverseKadane(arr,n)
    
    return max(k,rk)
    
GeeksforGeeks
