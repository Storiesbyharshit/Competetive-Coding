class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        AB = [a+b for a in A for b in B]
        CD = [c+d for c in C for d in D]
                
        # Two sum from AB and CD
        counts = 0
        CD_count = collections.Counter(CD)
        for num in AB:
            counts += CD_count.get(-num, 0)
                
        return counts
