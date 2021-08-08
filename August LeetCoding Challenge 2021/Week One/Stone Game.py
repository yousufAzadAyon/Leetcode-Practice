class Solution:
    def stoneGame(self, P):
        @lru_cache(None)
        def dp(i, j): 
            if i == j: return P[i]
            return max(P[i] - dp(i+1, j), P[j] - dp(i, j-1))
        
        return dp(0, len(P) - 1) > 0