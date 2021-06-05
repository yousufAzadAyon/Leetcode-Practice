class Solution:
    def maxPerformance(self, n: int, speed, efficiency, k: int) -> int:
        
        modulo = 10 ** 9 + 7

        new = list(zip(efficiency,speed))
        
        new.sort(reverse = True)
        
        result = 0
        sped = 0
        res = []
        
        for e,s in new:
            
            if len(res) > k-1:
                sped -= heapq.heappop(res)
            heapq.heappush(res,s)
            sped+=s
            result = max(result,sped*e)
        return result%modulo