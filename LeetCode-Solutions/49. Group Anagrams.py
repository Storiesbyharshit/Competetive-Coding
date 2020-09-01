class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        ans = []
        
        for word in strs:
            sorted_word = "".join(sorted(word))
            
            if sorted_word not in d:
                d[sorted_word] = [word]
            else:
                d[sorted_word].append(word)
            
        for key in d:
            ans.append(d[key])
        
        return ans
        
