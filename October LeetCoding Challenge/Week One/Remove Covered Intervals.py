class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:[x[0], -x[1]])
        ans, prev = 1, 0
        for i in range(1, len(intervals)):
            if intervals[i][1] > intervals[prev][1]:
                ans += 1
                prev = i
        return ans    