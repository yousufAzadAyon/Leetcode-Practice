class Solution:
    def removeDuplicates(self, nums):
        pos = 0
        prev = False
        while len(nums) > pos + 1:
            if nums[pos] == nums[pos + 1]:
                if prev:
                    nums.pop(pos + 1)
                    continue
                else:
                    prev = True
            if nums[pos] != nums[pos + 1]:
                prev = False
            pos += 1
            
        return len(nums)
