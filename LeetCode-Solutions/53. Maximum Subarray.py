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
    
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        maxend = nums[0]
        
        for i in range(1,len(nums)):
            maxend = max(maxend+nums[i],nums[i])
            res = max(res,maxend)
        return res
            
