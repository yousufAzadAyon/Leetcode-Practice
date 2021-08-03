class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        def dfs(start, end, cur):
            
			# add current subset to result
            result.append( cur[::] )
            
            for i in range(start, end+1):
                
                if i > start and nums[i] == nums[i-1]:
                    # skip duplicate subset
                    continue
                
                # select current number
                cur.append( nums[i] )
                
                # keep making subset in DFS
                dfs(start=i+1, end=end, cur=cur)
                
                # undo selection
                cur.pop()
        
        # keep nums in sorted with ascending order
        nums.sort()
        
        dfs( start=0, end=len(nums)-1, cur=[] )
        return result