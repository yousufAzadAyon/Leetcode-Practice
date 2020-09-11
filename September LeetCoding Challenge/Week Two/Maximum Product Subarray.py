class Solution:
    def maxProduct(self, nums):
        if len(nums) == 0:
            return 0

        max_so_far = nums[0]
        min_so_far = nums[0]
        result = max_so_far
        
        for i in range(1, len(nums)):
            curr = nums[i]
            temp_max = max(curr, curr*max_so_far, curr* min_so_far)
            min_so_far = min(curr, curr*max_so_far, curr* min_so_far)
            max_so_far = temp_max
            
            result = max(result, max_so_far)
            
        return result