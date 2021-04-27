class Solution:
    def solveNQueens(self, n: int):
        def checkBoard(board, row, col):
            for i in range(n):
                if i != row:
                    if board[i][col] == 'Q':
                        return False
                if i != col:    
                    if board[row][i] == 'Q':
                        return False
            directions = [(-1,1),(1,-1),(1,1),(-1,-1)]
            for rowD, colD in directions:
                r, c = row, col
                while 0<=r<n and 0<=c<n:
                    if r != row and c != col:
                        if board[r][c] == 'Q':
                            return False
                    r+=rowD    
                    c+=colD       
            return True 
        board = [["."] * n for _ in range(n)]
        ans = []
        def bt(row, board):
            if row == n:
                ans.append([''.join(r) for r in board])    
                return 
            for i in range(n):
                board[row][i] = 'Q'
                if checkBoard(board, row, i):
                    bt(row+1, board)
                board[row][i] = '.'    
        bt(0,board)        
        return ans        