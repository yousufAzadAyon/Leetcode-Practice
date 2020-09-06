class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        if not A:
            return 0
        
        total = 0
        for i in range(len(A)):
            
            for j in range(len(A[0])):
                total = max(total, max(self.count(B, A, i, j), self.count(A, B, i, j)))
        return total
                
    def count(self, A, B, i, j):
        total = 0
        
        for x in range(len(A)):
            
            for y in range(len(A[0])):
                if x + i >= len(A) or y + j >= len(A[0]):
                    continue
                
                if A[x][y] and B[x+i][y+j]:
                    total += 1
                    
                    
        return total