class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n, m, l = len(s1), len(s2), len(s3)
        dp = [None for j in range(m+1)]
        for i,j in itertools.product(reversed(range(n+1)), reversed(range(m+1))):
            dp[j] = (
                (i < n and i+j < l and s1[i] == s3[i+j] and dp[j]) or
                (j < m and i+j < l and s2[j] == s3[i+j] and dp[j+1]) or
                (i == n and j == m and i+j == l)
            )
        return dp[0]