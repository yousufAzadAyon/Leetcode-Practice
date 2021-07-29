class Solution:
    def beautifulArray(self, N):
        @lru_cache(None)
        def dfs(N):
            if N == 1: return (1,)
            t1 = dfs((N+1)//2)
            t2 = dfs(N//2)
            return [i*2-1 for i in t1] + [i*2 for i in t2]
        
        return dfs(N)