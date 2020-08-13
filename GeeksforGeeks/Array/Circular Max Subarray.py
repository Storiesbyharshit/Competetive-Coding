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
    
#
#

#
#
#Complete this function
def normalmaxsum(arr,n):
    res=arr[0]
    maxend=arr[0]
    for i in range(1,n):
        maxend=max(arr[i]+maxend,arr[i])
        res=max(res,maxend)
    return res    
def circularSubarraySum(arr,n):
    ##Your code here
    max_normal=normalmaxsum(arr,n)
    if max_normal<0:
        return  max_normal
    arr_sum=0
    for i in range(0,n):
        arr_sum+=arr[i]
        arr[i]=-arr[i]
    max_cir=arr_sum+ normalmaxsum(arr,n)
    return max(max_normal,max_cir)
