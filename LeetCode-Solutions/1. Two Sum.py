class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        d = dict()
        for i in range(len(nums)):
            num = nums[i]
            c = target - num
            if num not in d:
                d[c] = i
            else:
                return ([d[num],i])
            
