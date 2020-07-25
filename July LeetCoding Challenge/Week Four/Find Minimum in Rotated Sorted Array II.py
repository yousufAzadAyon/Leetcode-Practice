class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return -1
        n = len(nums)
        i = n-1
        while i >= 0 and nums[i] == nums[0]:
            i -= 1
        if nums[i] > nums[0]:
            return nums[0]
        l, r = 0, i
        while l<r:
            mid = (l+r)//2
            if nums[mid] >= nums[0]:
                l = mid+1
            else:
                r = mid
        return nums[l]