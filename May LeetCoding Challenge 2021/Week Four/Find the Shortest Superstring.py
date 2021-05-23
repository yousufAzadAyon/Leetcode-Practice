class Solution:
    def shortestSuperstring(self, words) -> str:
        n = len(words)
        overlaps = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                x, y = words[i], words[j]
                size = len(x)
                for k in range(1, size):
                    if y.startswith(x[k:]):
                        overlaps[i][j] = size - k
                        break

        @lru_cache(None)
        def helper(i, mask):
            if mask == (1<<n) - 1:
                return words[i]
            ans = '#' * 320
            for j in range(n):
                if mask & (1<<j) == 0:
                    k = overlaps[i][j]
                    string = helper(j, mask | (1<<j))
                    if len(words[i] + string[k:]) < len(ans):
                        ans = words[i] + string[k:]
            return ans

        return min([helper(i, 1<<i) for i in range(n)], key=len)