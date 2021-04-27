class Solution:
    def permute(self, nums):
        p=[]
        def rec(nums,i):
            if i==len(nums)-1:
                p.append(nums[:])
                return
            for j in range(i,len(nums)):
                nums[i],nums[j]=nums[j],nums[i]
                rec(nums,i+1)
                nums[i],nums[j]=nums[j],nums[i]
        rec(nums,0)
        return p