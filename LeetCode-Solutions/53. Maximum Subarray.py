class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        globalmax = max(nums)
        localmax = 0
        
        for i in range(len(nums)):
            num = nums[i]
            localmax = localmax + num
            globalmax = max(localmax,globalmax)
            
            if localmax < 0:
                localmax = 0
            
        return globalmax
            
