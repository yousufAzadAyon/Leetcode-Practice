class Solution:
    def hIndex(self, c: List[int]) -> int:
    	L = len(c)
    	for i,j in enumerate(sorted(c)):
    		if L - i <= j: return L - i
    	return 0