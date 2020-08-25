def caseSort(s,n):
    upper=[] #list containing uppercase letters
    lower=[]  #list containing lowercase letters

    for char in s:
        if(Case(char)):
            upper.append(char)
        else:
            lower.append(char)
    upper.sort(reverse=True)
    lower.sort(reverse=True)

    sorted_string=""
    for char in s:
        if(Case(char)):
            sorted_string+=upper.pop()
        else:
            sorted_string+=lower.pop()
    return sorted_string
    
def Case(c):
    #returns 1 if upper case and 0 for lower case
    if(ord(c)<=ord('Z') and ord(c)>=ord('A')):
        return 1
    return 0
