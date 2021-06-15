class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        res = 0
        for num, val in sorted(boxTypes, key=lambda x: -x[1]):
            if truckSize >= num:
                res += num * val
                truckSize -= num
            else:
                res += truckSize * val
                return res
        return res