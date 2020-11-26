class Solution:
    def canJump(self, n: List[int]) -> bool:
    	m = 0
    	for i in range(len(n)-1):
    		m = max(m, n[i] + i)
    		if n[i] != 0: continue
    		if m <= i: return False
    	return True