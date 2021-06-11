class Solution:
    def stoneGameVII(self, stones) -> int:
        n = len(stones)
        dp = [0] * n

        for i in range(n - 1, -1, -1):
            v = stones[i]
            run_sum = 0
            for j in range(i + 1, n):
                new_run = run_sum + stones[j]
                dp[j] = max(new_run - dp[j], run_sum + v - dp[j - 1])
                run_sum = new_run
        return dp[n - 1]