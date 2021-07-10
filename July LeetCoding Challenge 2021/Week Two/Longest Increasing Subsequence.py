class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res=[nums[0]]
        for i in nums[1:]:
            if i>res[-1]:
                res.append(i)
            else:
                res[bisect_left(res, i)]=i
        return len(res)