class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 1: return 0
        dp = [0] * len(prices)
        max_val = 0
        for i in range(len(prices)-1):
            for j in range(i+1, len(prices)):
                if prices[j] < prices[i]: 
                    dp[j] = dp[j-1]
                    break
                dp[j] = max(dp[j], # current val
                            prices[j]-prices[i] + # selling on jth day + best value before cool off
                            (dp[i-2] if (i-2) >=0 else 0), 
                           dp[j-1]) # remembering the previous best value
        return dp[-1]