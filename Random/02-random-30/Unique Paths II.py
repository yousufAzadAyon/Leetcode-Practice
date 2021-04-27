class Solution:
    def uniquePathsWithObstacles(self, obs):
        memo = {}
        m,n = len(obs), len(obs[0])
        def travel(m,n):
            if (m,n) in memo:
                return memo[(m,n)]
            if obs[m-1][n-1] ==1 :
                return 0
            if m==1 and n==1:
                return 1
            if m==0 or n==0:
                return 0
            val = travel(m-1, n) + travel(m,n-1)
            memo[(m,n)] = val
            return val
        return travel(m,n)