class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        alen, blen = len(A), len(B)
        if alen != blen:
            return -1
        elif alen == 0:
            return 0
        
        cand1, cand2 = A[0], B[0]
        
        res1 = self.helper(A, B, cand1)
        res2 = self.helper(B, A, cand1)
        if cand1 != cand2:
            res3 = self.helper(A, B, cand2)
            res4 = self.helper(B, A, cand2)
        else:
            res3 = -1
            res4 = -1
            
        res = -1
        for r in [res1, res2, res3, res4]:
            if r != -1:
                res = r if res == -1 else min(r, res)
        return res
                
    def helper(self, A, B, cand):
        res = 0
        for i in range(len(A)):
            if A[i] == cand:
                continue
            elif B[i] == cand:
                res += 1
            else:
                return -1
        return res