class Solution:
    def reverse(self, x: int) -> int:
        negFlag = 1
        if x < 0:
            negFlag = -1
            strx = str(x)[1:]
        else:
            strx = str(x)

        x = int(strx[::-1])  #reversing the string
        
        return 0 if x > pow(2, 31) else x * negFlag 
    
class Solution:
    def reverse(self, x: int) -> int:
        neg = False 
        if x < 0:
            neg = True
            x *= -1
        res = 0
        while x > 0:  #reversing
            res = res * 10 + x%10
            x = x//10
            
            
        if res > 2**31:
            return 0
        if neg:
            return -res 
        return res 
