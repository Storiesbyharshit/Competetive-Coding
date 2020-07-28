class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle)==0:
            return 0
        if needle not in haystack:
            return -1
        hlen = len(haystack)
        nlen = len(needle)
        
        for i in range(hlen):
            if needle == haystack[i:i+nlen]:
                return i 
                break
                
