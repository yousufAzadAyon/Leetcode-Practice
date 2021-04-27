class Solution:
    def nextPermutation(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        def find_swap(nums):
            start = len(nums) - 2
            for i in range(start, -1, -1):
                flag, mini = 0, float('inf')
                for j in range(i + 1, start + 2):
                    if nums[j] > nums[i] and nums[j] <= mini:
                        flag = 1
                        mini, loc = nums[j], j
                if flag:
                    return i, loc
            return -1, -1
        i, j = find_swap(nums)
        
        if i == j == -1:
            nums.sort()
        else:
            nums[i], nums[j] = nums[j], nums[i]
            nums[i + 1:] = nums[-1:i:-1]