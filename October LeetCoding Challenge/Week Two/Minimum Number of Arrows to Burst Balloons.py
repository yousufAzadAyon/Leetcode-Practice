class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points) == 0:
            return 0
        points.sort(key=lambda x : x[1])
        ans = 1
        lst = points[0][1]
        for pt in points:
            if pt[0] <= lst:
                continue
            else:
                ans += 1
                lst = pt[1]
        return ans