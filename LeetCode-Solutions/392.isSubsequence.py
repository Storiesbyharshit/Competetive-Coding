class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
		
		# two-pointers, one for s, the other for t
        idx_s, idx_t = 0, 0
		
        len_s, len_t = len(s), len(t)
        
		# linear scan from head
        while idx_s < len_s and idx_t < len_t:
            
            if s[idx_s] == t[idx_t]:
				# matched one character
				# s go to next position
                idx_s += 1
            
			# t go to next position
            idx_t += 1

		# check all character of s are matched
        return idx_s == len_s
        
