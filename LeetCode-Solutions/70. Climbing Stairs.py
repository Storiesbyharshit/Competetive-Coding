class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1 or n == 2 :
            return n
        dp = {}
        dp[1]=1
        dp[2]=2
        
        for i in range(3,n+1):
            dp[i] = dp[i-2]+dp[i-1]
        return dp[n]
