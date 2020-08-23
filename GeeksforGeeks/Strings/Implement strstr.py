"""
Implement strstr 
Your task is to implement the function strstr. The function takes two strings as 
arguments (s,x) and  locates the occurrence of the string x in the string s. 
The function returns and integer denoting the first occurrence of the string x in s (0 based indexing).
"""

def strstr(s,p):
    ind_s = 0 # current index in s.

    while ind_s < len(s):
        if s[ind_s] == p[0] :
            ind_p = 0  # current index in p.
            temp_s = ind_s

            while temp_s < len(s) and s[temp_s] == p[ind_p]:
                ind_p += 1
                temp_s += 1

                if ind_p == len(p): # match is found at ind_s - temp_s.
                    return ind_s
        ind_s += 1
        
    return -1
