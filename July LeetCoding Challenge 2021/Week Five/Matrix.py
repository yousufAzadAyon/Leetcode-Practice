class Solution:
    def updateMatrix(self, M):
        m, n, queue, visited = len(M), len(M[0]), deque(), set()
        for y, x in product(range(m), range(n)):
            if M[y][x] == 0: 
                queue.append((y, x))
                visited.add((y, x))
                
        dirs = [[1,0],[-1,0],[0,1],[0,-1]]
        level = 0
        
        while queue:
            level += 1
            for _ in range(len(queue)):
                y, x = queue.popleft()
                for dy, dx in dirs:
                    if 0<=y+dy<m and 0<=x+dx<n and (y+dy, x+dx) not in visited:
                        M[y+dy][x+dx] = level
                        queue.append((y+dy, x+dx))
                        visited |= {(y+dy, x+dx)}
        
        return M