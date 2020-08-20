#User function Template for python3


def maximumSum(arr,sizeOfArray):
    dp=[0]*(sizeOfArray+1)
    dp[0]=max(dp[0],arr[0])
    
    if(sizeOfArray>1) :
        dp[1]=max(dp[0],arr[1])
        
    for i in range(2,sizeOfArray):
        dp[i]=max(dp[i-2]+arr[i],dp[i-1])
       
        
    isAllNegative=True
    maxx=max(arr)
    
    for i in arr:
        if i>0:
            isAllNegative=False
            break;
        
    if isAllNegative==True:
        return maxx
    else:
        return dp[sizeOfArray-1]


