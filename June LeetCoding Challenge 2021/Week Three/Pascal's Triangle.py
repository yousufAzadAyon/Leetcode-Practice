from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(1,numRows+1):
            l = []
            for j in range(1,i+1):
                if j==1 or j==i:
                    l.append(1)
                else:
                    l.append(res[-1][j-i-1]+res[-1][j-i])
            res.append(l)
        return res