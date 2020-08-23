def checkPangram(s):
    temp='abcdefghijklmnopqrstuvwxyz'
    temp1=s.lower()
    for i in temp:
        if i not in temp1:
            return(0)
    return(1)
    

def checkPanagram(s):
    #code here
    alpha = [chr(c) for c in range(ord('a'),ord('z')+1)]
    for item in alpha:
        if item not in s:
            return False
    return True
        
        
        
def checkPanagram(s):
    #code here
    l=len(s)
    if l<26:
        return 0
    else:
        k=set(s)
        if len(k)>=26:
            return 1
        else:
            return 0



def checkPanagram(s):
    #code here
    li = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    s.lower()
    flag = 1
    for i in range(26):
        if li[i] in s:
            flag=0
        else:
            flag = 1
            break;
    if flag==0:
        return 1
    else:
        return 0
        
 def checkPangram(s):
    marked=[0 for i in range(26)]
    
    for char in s:
        if(ord(char)<=ord('Z') and ord(char)>=ord('A')):
            marked[ord(char)-ord('A')]=1
        elif(ord(char)<=ord('z') and ord(char)>=ord('a')):
            marked[ord(char)-ord('a')]=1
    
    for i in range(26):
        if(not marked[i]):
            return False
    return True
       
        
