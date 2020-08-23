#Python 3

'''
	Function to check if the given two strings
	are rotations of each other.
	Function Arguments: s1 and s2 (given strings)
	Return Type:boolean

	Contributed By: Nagendra Jha
'''
def areRotations(s1,s2):
    s=s1+s1
    '''adding the string allows to check for all cyclic rotations as
        every rotation is one of the strings of the double string'''
        
    if(len(s1)==len(s2) and s2 in s):
        return True
    return False
