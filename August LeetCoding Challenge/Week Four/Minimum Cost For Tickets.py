class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        if not days or not costs:
            return 0
        
        day_set = set()
        last_day = days[len(days)-1]
        dp = [0 for i in range(last_day+1)]
        
        for i in days:
            day_set.add(i)
            
        for i in range(1, len(dp)):
            if i not in day_set:
                dp[i] = dp[i-1]
            else:
                one_day = dp[i-1] + costs[0]
                seven_day = dp[max(i-7, 0)] + costs[1]
                thirty_day = dp[max(i-30, 0)] + costs[2]
                dp[i] = min(one_day, seven_day, thirty_day)
                
        
        return dp[last_day]