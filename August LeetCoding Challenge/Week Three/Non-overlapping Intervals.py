class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        i=1
        cnt=0
        while i<len(intervals) :
            if intervals[i][0]<intervals[i-1][1] :
                intervals.pop(i)
                cnt+=1
            else :
                i+=1
        return cnt