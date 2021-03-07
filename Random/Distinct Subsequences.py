class Solution:
    def numDistinct(self, source: str, target: str) -> int:
        dp = [0]*(len(target)+1)
        dp[0] = 1
        indexes = {}
        for i, c in enumerate(target):
            if c not in indexes:
                indexes[c] = []
            indexes[c].append(i+1)
        for v in indexes.values():
            v.reverse()   
        for c in source:
            if c in indexes:
                for i in indexes[c]:
                    dp[i] += dp[i-1]
        return dp[len(target)]