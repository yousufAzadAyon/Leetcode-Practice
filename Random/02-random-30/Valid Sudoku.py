class Solution:
	def isValidSudoku(self, board):
		for i in range(9):
			li={}
			for j in range(9):
				if board[i][j] in li and board[i][j]!='.':
					return False
				li[board[i][j]]=1
		for i in range(9):
			li={}
			for j in range(9):
				if board[j][i] in li and board[j][i]!='.':
					return False
				li[board[j][i]]=1
		for i in range(9):
			li={}
			for j in range(9):
				x=(i%3)*3+j%3
				y=(i//3)*3+j//3
				if board[x][y] in li and board[x][y]!='.':
					return False
				li[board[x][y]]=1
		return True