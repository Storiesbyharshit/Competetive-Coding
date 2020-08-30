class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return intervals
			
        intervals.sort(key=lambda x: x[0])
		
        ans = [intervals[0]]
        for start, end in intervals[1:]:
            if start <= ans[-1][1]:
                ans[-1][1] = max(end, ans[-1][1])
            else:
                ans.append([start, end])
				
        return ans
