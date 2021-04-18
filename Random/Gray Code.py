class Solution(object):
    def grayCode(self, n):
        if n == 0:
            return [0]
        if n == 1:
            return [0, 1]
        
        prev = ['0', '1']
        for i in range(1, n):
            new = ['0' + val for val in prev]
            prev = new + ['1' + val for val in prev[::-1]]
            
        return [int(x, 2) for x in prev]
