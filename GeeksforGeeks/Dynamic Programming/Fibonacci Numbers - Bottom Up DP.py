# Fibonacci Numbers - Bottom Up DP 
One of the rudimentary problems to understand DP is finding the nth Fibonacci number. Here, we will solve the problem using a bottom-up approach.
You are given a number N. You need to find the Nth Fibonacci number. The first two number of the series are 1 and 1.


def findNthFibonacci(number):
    dp=[0]*100
    if(dp[number]>0):
        return dp[number]
    dp[0]=0
    dp[1]=1
    
    for i in range(2,number+1):
        
        # We need to add the below line to do
        # bottom up computations
        dp[i] = dp[i-1] + dp[i-2]
        
    return dp[number]
