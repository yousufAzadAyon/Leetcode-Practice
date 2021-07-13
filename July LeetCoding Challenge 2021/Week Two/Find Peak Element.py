class Solution:
    def findPeakElement(self, nums) -> int:
        for i,j in enumerate(nums):
            if j == max(nums):
                return i