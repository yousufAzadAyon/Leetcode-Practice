class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        diff_list = list()
        if len(nums) < 2:
            return 0
        elif len(nums) == 2:
            return nums[1]-nums[0]
        else:
            nums.sort()
            for i in range(len(nums) - 1):
                diff_list.append(nums[i+1] - nums[i])
            return max(diff_list)