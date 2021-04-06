class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums or len(nums) == 0 or target < nums[0] or target > nums[-1]:
            return [-1, -1]
        
        left, right = 0, 0
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] >= target:
                end = mid - 1
            else:
                start = mid + 1
        if nums[start] == target:
            left = start
        elif nums[end] == target:
            left = start
        else:
            return [-1, -1]
        
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] <= target:
                start = mid + 1
            else:
                end = mid - 1
        if nums[end] == target:
            right = end
        elif nums[start] == target:
            right = start
        
        return [left, right]