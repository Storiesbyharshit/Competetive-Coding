class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        start = ans = 0
        for i,c in enumerate(s):
            if c in seen and start<=seen[c]:
                start = seen[c]+1
            else:
                ans = max(ans,i-start+1)
            seen[c] = i
        return ans
        
        
class Solution(object):
    def lengthOfLongestSubstring(self, s):

        if len(s) == 0:
            return 0
        seen = {}
        left, right = 0, 0
        longest = 1
        while right < len(s):
            if s[right] in seen:
                left = max(left,seen[s[right]]+1)
            longest = max(longest, right - left + 1)
            seen[s[right]] = right
            right += 1
            print(left, right, longest)
        return longest
