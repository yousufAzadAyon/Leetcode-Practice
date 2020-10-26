class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [0] * (query_row + 1)
        dp[0] = poured
        
        for i in range(query_row):
            for j in range(i, -1, -1):
                overflow = max(0, dp[j] - 1)
                if j + 1 <= query_row:
                    dp[j+1] += overflow / 2
                dp[j] = overflow / 2
        
        if dp[query_glass] >= 1:
            return 1
        else:
            return dp[query_glass]