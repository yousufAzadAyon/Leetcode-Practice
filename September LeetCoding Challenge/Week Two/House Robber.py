class Solution:
    def rob(self, nums):
        n = len(nums)
        dp = [0] * (n + 2)
        for i in range(n):
            dp[i + 2] = max(dp[i + 1], dp[i] + nums[i])
        
        return dp[-1]