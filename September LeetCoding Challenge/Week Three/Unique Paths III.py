from functools import lru_cache
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        n = len(grid)
        m = len(grid[0])
        empty_cells, ind = 0, [-1, -1]
        paths = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        
        for i in range(n):
            for j in range(m):
				# know the starting point
                if grid[i][j] == 1:
                    ind = [i, j]
				# count the number of cells having '0'
                elif grid[i][j] == 0:
                    empty_cells += 1
                else:
                    pass
        visited = [[0]*m for i in range(n)]
		# mark the starting point as visited
        visited[ind[0]][ind[1]] = 1
        print(empty_cells)
        def dfs(i, j, rem):
		# if cell cant be walked or we havent walked through all the cells with value '0'
            if grid[i][j] == -1 or (grid[i][j] == 2 and rem != -1):
                return 0
			# if reached the target by walking through all the empty cells 
            elif grid[i][j] == 2 and rem == -1:
                return 1
            else:
			# have count of the number of paths we can have from cell [i, j]
                count = 0
                for x, y in paths:
                    nx, ny = x + i, y + j
                    if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                        visited[nx][ny] = 1
                        count += dfs(nx, ny, rem - 1)
                        visited[nx][ny] = 0
            return count
			
			# call dfs function
        ans = dfs(ind[0], ind[1], empty_cells)
        return ans