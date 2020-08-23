def findSum(s):
    #code here
    x = []
    key = 0
    i = 0
    while i < len(s): 
        if s[i].isnumeric():
            x.append(int(s[i]))
            i += 1
            while i < len(s) and s[i].isnumeric():
                x[key] = x[key]*10 + int(s[i])
                i += 1
            key += 1
        i += 1
    return sum(x)
    
    
    
    
import re
def findSum(s):
    #code here
    return sum(map(int,re.findall('\d+',s))) 
