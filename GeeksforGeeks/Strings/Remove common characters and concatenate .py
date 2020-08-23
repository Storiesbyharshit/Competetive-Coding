def concatenatedString(s,p):
    #code here
    cms = set(s) & set(p)
    rst = []
    for i in s:
        if i not in cms:
            rst.append(i)
    for i in p:
        if i not in cms:
            rst.append(i)
    if len(rst) == 0:
        return -1
    else:
        return ''.join(rst)
    
	
def concatenatedString(s,p):
    #code here
    occurrence_s=[0 for i in range(256)]
    occurrence_p=[0 for i in range(256)]
    
    # storing the count of chars in s1
    for i in range(len(s)):
        occurrence_s[ord(s[i])]+=1
        
    # storing the count of chars in p
    for i in range(len(p)):
        occurrence_p[ord(p[i])]+=1
    
    concatenated_str=""
    
    # Find characters of s1 that are not
	# present in s2 and append to result
    for i in range(len(s)):
        if(occurrence_p[ord(s[i])]==0):
            concatenated_str+=s[i]
    
    # Find characters of s2 that are not 
	# present in s1.
    for i in range(len(p)):
        if(occurrence_s[ord(p[i])]==0):
            concatenated_str+=p[i]
            
    if(len(concatenated_str)):
        return concatenated_str
    return -1
    
