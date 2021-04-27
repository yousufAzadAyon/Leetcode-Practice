class Solution:
    def merge(self, intervals):
        """
        Time Complexity: O(n log n)
        Space: O(log N) or O(n)
        """
        if not intervals:
            return []
        intervals.sort(key=lambda x: x[0])
        result=[]
        pivot = intervals[0]
        
        for i in range(1,len(intervals)):
            if pivot[1] < intervals[i][0]:
                # if end of base is less than start of next interval
                result.append(pivot)
                pivot = intervals[i]
            else:
                # if there is an overlap then get the min and max
                pivot[0]=min(pivot[0],intervals[i][0])
                pivot[1]=max(pivot[1], intervals[i][1])
        result.append(pivot)
        return result