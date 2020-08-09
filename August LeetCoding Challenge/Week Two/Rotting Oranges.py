class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten = []
        rows = len(grid)
        columns = len(grid[0])
        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == 2:
                    rotten.append((i, j))

        def add_neighbors(rotten):
            neighbors = []
            for i, j in rotten:
                if i > 0 and grid[i - 1][j] == 1:
                    neighbors.append((i - 1, j))
                    grid[i-1][j] = 2
                if j > 0 and grid[i][j - 1] == 1:
                    neighbors.append((i, j - 1))
                    grid[i][j-1] = 2
                if i < rows - 1 and grid[i + 1][j] == 1:
                    neighbors.append((i + 1, j))
                    grid[i + 1][j] = 2
                if j < columns - 1 and grid[i][j + 1] == 1:
                    neighbors.append((i, j + 1))
                    grid[i][j+1] = 2
            return neighbors

        minutes = 0
        while (1):
            rotten = add_neighbors(rotten)
            if len(rotten) == 0:
                break
            minutes += 1

        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == 1:
                    return -1

        return minutes