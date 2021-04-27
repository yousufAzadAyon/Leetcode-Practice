class Solution:
    def removeDuplicates(self, nums):
        if len(nums) == 1:
            return 1
        else:
            i = 0
            label = None
            
            for j in range(1, len(nums)):
                if nums[i] == nums[j] != label:
                    i += 1
                    nums[i] = nums[j]
                    label = nums[i]

                elif nums[i] != nums[j]:
                    i += 1
                    nums[i] = nums[j]

            return i+1
