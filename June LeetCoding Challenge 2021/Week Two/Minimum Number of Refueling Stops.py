class Solution:
    def minRefuelStops(self, target: int, start_fuel: int, stations: List[List[int]]) -> int:
        hp, ans, can_reach = [], 0, start_fuel
        heapq.heapify(hp)
        for pos, fuel in stations:
            if can_reach >= target:
                return ans
            elif pos <= can_reach:
                heapq.heappush(hp, -fuel)
            else:
                while len(hp) > 0:
                    bigger = -heapq.heappop(hp)
                    can_reach += bigger
                    ans += 1
                    if can_reach >= pos:
                        break
                if can_reach < pos:
                    return -1
                heapq.heappush(hp, -fuel)
        if can_reach >= target:
            return ans
        while len(hp) > 0:
            bigger = -heapq.heappop(hp)
            can_reach += bigger
            ans += 1
            if can_reach >= target:
                break
        if can_reach < target:
            return -1
        return ans