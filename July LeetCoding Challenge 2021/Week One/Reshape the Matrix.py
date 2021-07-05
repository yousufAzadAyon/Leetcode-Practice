class Solution:
    def matrixReshape(self, mat, r: int, c: int):
        m = len(mat)
        n = len(mat[0])
        if m * n == r * c:
            result = []
            row = 0
            col = 0
            for i in range(r):
                result.append([])
                for j in range(c):
                    result[i].append(mat[row][col])
                    col = col + 1
                    if col == n:
                        col = 0
                        row = row + 1
            return result
        else:
            return mat