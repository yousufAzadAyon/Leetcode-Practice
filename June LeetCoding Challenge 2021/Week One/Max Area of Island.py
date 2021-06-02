class Solution:
    def maxAreaOfIsland(self, G: List[List[int]]) -> int:
    	M, N, m = len(G), len(G[0]), 0
    	def area(x,y):
    		p, t, a, G[x][y] = [[x,y]], [], 1, 0
    		while p:
    			for i,j in p:
    				for k,l in [[i-1,j],[i,j+1],[i+1,j],[i,j-1]]:
    					if k in [-1,M] or l in [-1,N] or G[k][l] == 0: continue
    					a, G[k][l], _ = a + 1, 0, t.append([k,l])
    			p, t = t, []
    		return a
    	for i,j in itertools.product(range(M),range(N)):
    		if G[i][j]: m = max(m,area(i,j))
    	return m