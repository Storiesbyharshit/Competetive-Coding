class Solution:
    def minPathSum(self, g: List[List[int]]) -> int:
        n=len(g)
        m=len(g[0])
        dp=[[sys.maxsize for i in range(m+1)]for j in range(n+1)]
        
        dp[0][1]=0
        dp[1][0]=0
        for i in range(1,n+1):
            for j in range(1,m+1):
                dp[i][j]=g[i-1][j-1]+min(dp[i-1][j],dp[i][j-1])
        
        return dp[n][m]
