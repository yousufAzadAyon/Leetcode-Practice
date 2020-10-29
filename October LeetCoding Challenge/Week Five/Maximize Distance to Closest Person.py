class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        
        prev = None
        diff = 0
        result = -1
        
        n = len(seats)
        for i in range(n):
            if seats[i]:
                if prev is None:
                    prev = i
                    left = i
                elif i-prev > diff:
                    diff = i-prev
                    result = diff // 2
                prev = i
        
        right = n - prev - 1
        
        return max(left, right, result)