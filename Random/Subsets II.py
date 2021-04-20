class Solution:
    def subsetsWithDup(self, nums):
        result = []
                
        def dfs(start, end, cur):
            result.append( cur[::] )
            
            for i in range(start, end+1):
                
                if i > start and nums[i] == nums[i-1]:
                    continue
                cur.append( nums[i] )
                dfs(start=i+1, end=end, cur=cur)
                cur.pop()
        nums.sort()
        
        dfs( start=0, end=len(nums)-1, cur=[] )
        return result