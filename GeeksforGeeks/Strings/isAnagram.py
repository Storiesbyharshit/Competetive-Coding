#Python 3

'''Function to check given two strings
   are anagrams or not.
   a,b: given strings
'''
def isAnagram(a,b):
    mp = {}
    
    for i in a:
        if i in mp.keys ():
            mp[i] += 1
        else:
            mp[i] = 1
    
    for i in b:
        if i not in mp.keys ():
            return False
        else:
            mp[i] -= 1
            
    for i in mp.keys ():
        if mp[i] != 0:
            return False
            
    return True
