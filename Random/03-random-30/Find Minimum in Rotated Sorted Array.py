class Solution:
    def findMin(self, nums) -> int:
        # return min(nums)
        low = 0
        high = len(nums) - 1
        if nums[low] < nums[high]:
            return nums[low]
        while low < high - 1:
            mid = (high + low) // 2
            if nums[low] > nums[mid]:
                high = mid
            else:
                low = mid
        return nums[high]