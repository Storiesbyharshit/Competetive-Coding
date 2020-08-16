Coin Change - Minimum number of coins 
You are given an amount denoted by value. You are also given an array of coins. The array contains the denominations of the give coins. You need to find the minimum number of coins to make the change for value using the coins of given denominations. Also, keep in mind that you have infinite supply of the coins.



#User function Template for python3
import sys

##Complete this function
def minimumNumberOfCoins(coins,numberOfCoins,value):
    
    # your code here
    dp = [sys.maxsize]*(value+1)
    dp[0]=0
    
    for i in range(1, value+1):
        for j in range(numberOfCoins):
            if coins[j] <= i:
                t = dp[i-coins[j]]
                if t!=sys.maxsize and t+1<dp[i]:
                    dp[i]=t+1
    if dp[-1] == sys.maxsize:
        return -1
    return dp[-1]
