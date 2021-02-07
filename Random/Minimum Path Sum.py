import functools

class Solution:
    def minPathSum(self, grid):
        
        m = len(grid) - 1
        n = len(grid[0]) - 1
        
        @functools.lru_cache(maxsize=None)
        def get_min(m, n):
            if m == 0 and n == 0:
                return 0
            if m != 0 and n != 0:
                return min(grid[m][n] + get_min(m-1, n), grid[m][n] + get_min(m, n-1))
        
            if m == 0:
                return grid[m][n] + get_min(m, n-1)
            else:
                return grid[m][n] +  get_min(m-1, n)
                
        return get_min(m, n) + grid[0][0]