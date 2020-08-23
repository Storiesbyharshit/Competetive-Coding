def areIsomorphic(s,p):
    if len(s) != len(p):
        return False 
    arr1 = [0]*256
    arr2 = [0]*256
    for i in range(len(s)):
        arr1[ord(s[i])] += 1
        arr2[ord(p[i])] += 1
        if arr2[ord(p[i])] != arr1[ord(s[i])]:
            return False
    return True



def areIsomorphic(s,p):
    d1={}
    d2={}
    for i ,val in enumerate(s):
        d1[val]=d1.get(val,[])+[i]
        
    for j ,val in enumerate(p):
        d2[val]=d2.get(val,[])+[j]
    
    if(sorted(d1.values())==sorted(d2.values())):
        return 1
    else:
        return 0



# Python program to check if two strings are isomorphic 
MAX_CHARS = 256
  
# This function returns true if str1 and str2 are isomorphic 
def areIsomorphic(string1, string2): 
    m = len(string1) 
    n = len(string2) 
  
    # Length of both strings must be same for one to one 
    # corresponance 
    if m != n: 
        return False
  
    # To mark visited characters in str2 
    marked = [False] * MAX_CHARS 
  
    # To store mapping of every character from str1 to 
    # that of str2. Initialize all entries of map as -1 
    map = [-1] * MAX_CHARS 
  
    # Process all characters one by one 
    for i in xrange(n): 
  
        # if current character of str1 is seen first 
        # time in it. 
        if map[ord(string1[i])] == -1: 
  
            # if current character of st2 is already 
            # seen, one to one mapping not possible 
            if marked[ord(string2[i])] == True: 
                return False
  
            # Mark current character of str2 as visited 
            marked[ord(string2[i])] = True
  
            # Store mapping of current characters 
            map[ord(string1[i])] = string2[i] 
  
        # If this is not first appearance of current 
        # character in str1, then check if previous 
        # appearance mapped to same character of str2 
        elif map[ord(string1[i])] != string2[i]: 
            return False
  
    return True

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
            
        
        
