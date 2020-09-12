class Solution:
    def combinationSum3(self, k: int, n: int):
        src = [ *range(1, 10) ]
        result = []
        
        def dfs( cur, idx, target):
            
            if target < 0:
                return
            
            if len(cur) == k:
                if target == 0:
                    result.append( cur[::] )
                return
                
            for j in range(idx, len(src)):
                cur.append( src[j] )
                dfs( cur, j+1, target-src[j] )
                cur.pop()
            return
        
        dfs(cur=[], idx=0, target=n)
        return result