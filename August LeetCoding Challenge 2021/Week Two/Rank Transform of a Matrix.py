class Solution:
    def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
        n, m = len(matrix), len(matrix[0])
        rank = [0] * (m + n)
        d = collections.defaultdict(list)
        
        for i in range(n):
            for j in range(m):
                d[matrix[i][j]].append((i, j))
        
        def find(i):
            if p[i] != i:
                p[i] = find(p[i])
            return p[i]
        
        for a in sorted(d):
            p = [i for i in range(m+n)]
            rank2 = rank[:]
            for i, j in d[a]:
                i, j = find(i), find(j+n)
                p[i] = j
                rank2[j] = max(rank2[i], rank2[j])
            for i, j in d[a]:
                rank[i] = rank[j+n] = matrix[i][j] = rank2[find(i)] + 1
        
        return matrix