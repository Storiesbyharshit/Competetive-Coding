#User function Template for python3


def maximumSum(arr,sizeOfArray):
    dp=[0]*sizeOfArray##declaring dp array 
    dp[0]=arr[0]
    answer=dp[0]
    for i in range(1,sizeOfArray):
        ##The maximum sum at dp[i] will be max of (current array element+dp[i-1]) and (current array element)
        ##Complete this code
        answer=max(answer,dp[i])
    ##dp array print    
    for i in range(sizeOfArray):
        print(dp[i],end=" ")
    print()
    ##print end
    return answer


