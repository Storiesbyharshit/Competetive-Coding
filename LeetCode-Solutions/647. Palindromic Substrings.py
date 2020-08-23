class Solution:
    def countSubstrings(self, s: str) -> int:
        size = len(s)
        count=0
        dp = [[0]*(size) for _ in range(size)]
        for row in range(size):
            for col in range(row+1):
                dp[row][col] = s[row] == s[col] and (row - col <3  or dp[row-1][col+1])
                if dp[row][col]:
                    count+=1
        return count
