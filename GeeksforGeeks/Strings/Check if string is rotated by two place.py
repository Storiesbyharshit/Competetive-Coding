#Python 3

'''
	Function to check if the given string can be obtained
	by rotating other string 'p' by two places.

	Function Arguments: s (given string), p(string to be rotated)
	Return Type: boolean

	Contributed By: Nagendra Jha
'''

def isRotated(s,p):
    n=len(p)
    if(n<3):
        return p==s
    anticlock_str=p[2:]+p[0:2]
    clockwise_str=p[-2]+p[-1]+p[:n-2]
    
    if(s==anticlock_str or s==clockwise_str):
        return True
    return False
