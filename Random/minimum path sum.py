class Solution:
    def minPathSum(self, grid):
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i+j == 0):
                    continue
                if (i*j != 0):
                    grid[i][j] += min(grid[i-1][j], grid[i][j-1])
                elif (i == 0):
                    grid[i][j] += grid[i][j-1]
                elif (j == 0):
                    grid[i][j] += grid[i-1][j]

        return (grid[-1][-1])
