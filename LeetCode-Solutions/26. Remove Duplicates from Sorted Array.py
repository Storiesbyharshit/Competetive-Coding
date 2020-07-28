26. Remove Duplicates from Sorted Array
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx = 1
        for i in range(len(nums)-1):
            if nums[i] != nums[i+1]:
                nums[idx] = nums[i+1]
                idx += 1
        return idx
        
        
        
        
