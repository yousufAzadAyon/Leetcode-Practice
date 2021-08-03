class Solution:
    def twoSum(self, nums, target):
        for i, j in enumerate(nums):
            if nums[i]+nums[i+1] == target:
                return [i, i+1]