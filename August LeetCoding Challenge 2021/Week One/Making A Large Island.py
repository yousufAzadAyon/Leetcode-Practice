class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        def next_move(x,y):
            op = []
            for i,j in ((0,1),(1,0),(0,-1),(-1,0)):
                if 0 <= x+i < n and 0 <= y+j < n:
                    op.append([x+i, y+j]) 
            return op
        
        
        def dfs(i,j, marker):
            count = 0
            grid[i][j] = marker
            for x,y in next_move(i,j):
                if grid[x][y] == 1:
                    count += dfs(x,y,marker)
            return count + 1
        
            
        island_size ={}
        marker= 2
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    island_size[marker] = dfs(i, j, marker)
                    marker += 1
        if len(island_size) == 0:
            return 1
        max_size = max(island_size.values())
        # print(island_size, grid)
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    s=set()
                    local_size= 0
                    for x,y in next_move(i,j):
                        s.add(grid[x][y])

                    for m in s:
                        if m != 0:
                            local_size += island_size[m]
                    max_size = max(local_size+1, max_size)
        return max_size