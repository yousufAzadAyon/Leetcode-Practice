class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        if not matrix:
            return 0
        row_size, col_size = len(matrix), len(matrix[0])
        ans = float('-inf')
        for i in range(col_size):
            sm = [0] * row_size
            for j in range(i, col_size):
                for row in range(row_size):
                    sm[row] += matrix[row][j]
                res = float('-inf')
                cur = 0
                for x in sm:
                    if cur < 0:
                        cur = x
                    else:
                        cur += x
                    if cur > res:
                        res = cur
                if res <= k :
                    ans = max(ans, res)
                    continue
                cur, array, res = 0, [0], float('-inf')
                for x in sm:
                    cur += x
                    idx = bisect.bisect_left(array, cur-k)
                    if idx < len(array):
                        res = max(res, cur-array[idx])
                    bisect.insort(array, cur)
                ans = max(ans, res)
        return ans