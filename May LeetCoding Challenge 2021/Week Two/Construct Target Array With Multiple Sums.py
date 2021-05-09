from heapq import heappop, heappush
class Solution:
    def isPossible(self, target) -> bool:
        if len(target) == 1:
            return target == [1]
        s = sum(target)
        hp = []
        for x in target:
            if x != 1:
                heappush(hp, -x)
        while hp:
            x = -heappop(hp)
            y = -hp[0] if hp else 1
            p = (x - y) % (s - x) + y
            if p > 1:
                p -= (s - x)
            s = s - x + p
            if p < 1:
                return False
            if p > 1:
                heappush(hp, -p)
        return True