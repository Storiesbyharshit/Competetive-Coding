#9. Palindrome Number

class Solution:
    def isPalindrome(self, x: int) -> bool:
        strx = str(x)
        r = "".join(reversed(strx))
        return strx == r
    
    
class Solution:
    def isPalindrome(self, x: int) -> bool:
        res = 0
        ref = x
        while x > 0 :
            res = res * 10 + x%10
            x //= 10
        print (res)
        return res == ref
