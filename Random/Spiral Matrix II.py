class Solution:
    def generateMatrix(self, n: int):
        matrix = [[0]*n for i in range(n)] 
        nums = [num for num in range(2,n**2+1)]
        x = y = 0
        matrix[x][y] = 1 

        while nums:
	        while -1 < y+1 < n and matrix[x][y+1] == 0:
		        y = y+1
		        matrix[x][y] = nums.pop(0)
	        while -1 < x+1 < n and matrix[x+1][y] == 0:
		        x = x+1
		        matrix[x][y] = nums.pop(0)
	        while -1 < y-1 < n and matrix[x][y-1] == 0:
		        y = y-1
		        matrix[x][y] = nums.pop(0)
	        while -1 < x-1 < n and matrix[x-1][y] == 0:
		        x = x-1
		        matrix[x][y] = nums.pop(0)

        return matrix