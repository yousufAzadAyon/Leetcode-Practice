import imp
from itertools import accumulate
class NumMatrix:
    def __init__(self, matrix):
        self.data = []
        for x in matrix:
            self.data.append(list(accumulate(x)))

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:        
        res = 0
        for x in range(row1, row2+1):
            if col1 > 0:
                res += self.data[x][col2] - self.data[x][col1-1]
            else:
                res += self.data[x][col2] 
        return res