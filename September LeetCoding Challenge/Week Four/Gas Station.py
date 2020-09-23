class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        for i in range(n):
            if gas[i]>=cost[i]:
                tank = gas[i]-cost[i]
                j = i+1 if i<n-1 else 0
                while j!=i:
                    tank += gas[j]
                    if tank<cost[j]:
                        break
                    else:
                        tank -= cost[j]
                    if j<n-1:
                        j += 1
                    else:
                        j = 0
                if j==i:
                    return i
        return -1