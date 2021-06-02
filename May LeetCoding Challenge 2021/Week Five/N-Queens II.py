class Solution:
    def totalNQueens(self, n: int) -> int:
        col = [False]*(n)
        diag1 = [False]*(2*n)
        diag2 = [False]*(2*n)
        self.count = 0
        def backTrack(y):
            if(y==n):
                self.count+=1
            else:
                for x in range(0,n):
                    if(col[x] or diag1[x+y] or diag2[x-y+n-1]):continue
                    col[x],diag1[x+y],diag2[x-y+n-1]=1,1,1
                    backTrack(y+1)
                    col[x],diag1[x+y],diag2[x-y+n-1]=0,0,0
        backTrack(0)
        return self.count