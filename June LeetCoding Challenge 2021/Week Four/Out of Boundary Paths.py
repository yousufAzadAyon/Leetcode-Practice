class Solution:
    def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
        
        @lru_cache(None)
        def paths(i, j, moves):
            if i < 0 or j < 0 or i > m - 1 or j > n - 1:
                return 1
            elif moves == 0:
                return 0
            else:
                ans = \
                    paths(i - 1, j, moves - 1) + \
                    paths(i + 1, j, moves - 1) + \
                    paths(i, j - 1, moves - 1) + \
                    paths(i, j + 1, moves - 1)
                return ans % 1_000_000_007
            
        return paths(i, j, N)