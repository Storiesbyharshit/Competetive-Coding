#Python 3

'''
	Function to return the lefmost index of the repeating 
	character whose first appereance is left most or return
	-1 if all characters are distinct.
	
	Function Arguments: s (given string)
	Return Type: integer
	
'''

def repeatingCharacter(s):
    occurences=[0 for i in range(256)]
    
    for char in s:
        occurences[ord(char)]+=1
    
    for i in range(len(s)):
        if(occurences[ord(s[i])]>1):
            return i
    return -1
