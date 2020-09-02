 class Solution:
    def lengthOfLongestSubstring(self, string: str) -> int:

        lastIndex = [-1] * 256 

        n = len(string) 
        res = 0   # Result 
        i = 0

        for j in range(0, n): 
            # Find the last index of str[j] 
            # Update i (starting index of current window) 
            # as maximum of current value of i and last 
            # index plus 1 
            i = max(i, lastIndex[ord(string[j])] + 1); 

            # Update result if we get a larger window 
            res =  max(res, j - i + 1) 

            # Update last index of j. 
            lastIndex[ord(string[j])] = j; 

        return res 
