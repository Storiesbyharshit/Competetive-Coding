class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        
        
        
        if strs == []: #empty
            return ""
        
        if len(strs) == 1: #only one element 
            return strs[0]
        
        pref = strs[0] #setting first to be longest
        plen = len(pref)
        
        for i in strs[1:]: #iterating list of words from second to last
            
            while pref != i[0:plen]: #checking for same
                pref = pref[0:(plen-1)] #reducing the word 
                plen -=1 
                
            if pref == "":
                return ""
        return pref
