from collections import deque 
class Solution:
    def maxResult(self, nums, k: int) -> int:
        deq = deque()
        deq.append(0)
        
        dp = [0] * len(nums)
        dp[0] = nums[0]
        
        for i in range(1, len(nums)):
            dp[i] = dp[deq[0]] + nums[i]

            if deq[0] == i - k:
                deq.popleft()
            
            while deq and dp[deq[-1]] < dp[i]:
                deq.pop()
            
            deq.append(i)
        
        return dp[-1]
            