class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if not nums:
            return None
        
        diff=float('inf')
        nums.sort()
        
        for i in range(len(nums)-2):
            p1=i+1
            p2=len(nums)-1
            
            while p1<p2:
                s=nums[i]+nums[p1]+nums[p2]
                if abs(s-target) < diff:
                    diff=abs(s-target)
                    output=s
                
                if s<target:
                    p1+=1
                elif s>target:
                    p2-=1
                else:
                    return target
        return output      