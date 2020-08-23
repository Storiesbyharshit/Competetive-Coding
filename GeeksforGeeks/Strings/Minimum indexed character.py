def minIndexChar(s,p):
    present=set() #contains set of all characters in p 
    for char in p:
        present.add(char)
    i = 0
    for char in s:
        if(char in present):
            return i
        i+=1
    return -1
