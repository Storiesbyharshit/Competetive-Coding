class Solution:
    
    def longestPalindrome(self,s):

        def checkpalindrome(s,l,r):
            while l>= 0 and r<len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]
        
        result = ""
        for i in range(len(s)):
            odd = checkpalindrome(s,i,i)
            even = checkpalindrome(s,i,i+1)
            result = max(result,odd,even,key = len)
        return result
                       
    
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
		n = len(s)
        if n < 2: return s
        dp, ans = [[0]*n for _ in range(n)], {}
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and ((j - i + 1) <= 3 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    ans[j-i+1] = s[i:j+1]
                else:
                    dp[i][j] = False
        return ans[max(ans)]
