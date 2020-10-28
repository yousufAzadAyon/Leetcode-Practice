class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        s = set(nums)
        i = 0
        res = []
        while i < len(nums):
            j = nums[i]
            cnt = 0
            while j+1 in s:
                j += 1
                cnt += 1
            if cnt == 0:
                res.append(str(nums[i]))
            else:
                res.append(str(nums[i])+'->'+str(j))
            i += cnt+1
        return res