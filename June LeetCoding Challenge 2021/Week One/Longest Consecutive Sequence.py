class Solution:
    def longestConsecutive(self, nums) -> int:
        
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        
        #sorting
        nums.sort()
        count = 0
        ans = 0
        #print(nums)
        for i in range(len(nums)-1):
            if nums[i+1]-nums[i] == 1:
                count+=1
            elif nums[i+1]-nums[i] == 0:
                continue
            else:
                ans = max(ans,count+1)
                count = 0
        ans = max(ans,count+1)
        
        return ans