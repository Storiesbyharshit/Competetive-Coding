class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        index = 0
        
        for num in nums:
            if num >= target:
                return index
            index += 1
        
        if index == len(nums):
            return len(nums)

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            nums.append(target)
            nums.sort()
            return nums.index(target)
