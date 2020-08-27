class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        s = sorted([(it[0], i) for i, it in enumerate(intervals)])
        ans = []    
        for it in intervals:
            i = bisect.bisect_left(s, (it[1], -1))
            ans.append(s[i][1] if i < len(s) else -1)
        return ans