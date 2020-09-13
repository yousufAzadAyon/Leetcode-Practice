class Solution:
    def insert(self, intervals, newInterval):
        if not intervals:
            return [newInterval]
        merged = False
        temp = []
        
        for i in intervals:
            if not merged and newInterval[0] < i[0]:
                temp.append(newInterval)
                merged = True
            temp.append(i)
        if not merged:
            temp.append(newInterval)
        res = []
        
        for i in temp:
            if res and i[0] <= res[-1][-1]:
                res[-1][-1] = max(i[1], res[-1][-1])
            else:
                res += [i]
        return res