class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        maxNum=nums[0]
        maxAll=nums[0]
        ans=1
        for i in range(1,len(nums)):
            if nums[i]<maxNum:
                ans=i+1
                maxNum=maxAll
            else:
                maxAll=max(maxAll,nums[i])
        return ans