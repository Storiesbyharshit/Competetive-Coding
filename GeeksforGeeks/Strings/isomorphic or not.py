#Python 3
'''
	Function to check if the given strings are
	isomorphic or not.
	
	Function Arguments: s and p (given strings)
	Return Type: boolean

	Contributed By: Nagendra Jha
'''
def areIsomorphic(s,p):
    d=defaultdict(chr) #default dict to store mapping of characters
    
    if(len(s)  != len(p)):
        return False
    marked=[0 for i in range(26)] # to keep track of already visited characters
    
    for i in range(len(s)):
        c=s[i]
        c_p=p[i]
        if(c not in d):
            if(marked[ord(c_p)-ord('a')]):
                return False
            else:
                marked[ord(c_p)-ord('a')]=1
                d[c]=c_p
        else:
            if(d[c] != c_p):
                return False
    return True
            
        
        
