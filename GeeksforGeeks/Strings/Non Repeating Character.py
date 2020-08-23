#Python 3

'''
	Function to return the index of lefmost non-repeating 
	character or return
	-1 if all characters occur more than once.
	
	Function Arguments: s (given string) and n (length of string)
	Return Type: integer
	
	Contributed By: Nagendra Jha
'''

def nonrepeatingCharacter(s):
    occurences=[0 for i in range(256)]
    
    for char in s:
        occurences[ord(char)]+=1
    
    for i in range(len(s)):
        if(occurences[ord(s[i])]==1):
            return s[i]
    return '$'
    
