class Solution:
    def isIsomorphic(self, s, t):
        d1, d2 = {}, {}
        for i, j in zip(s,t):
            if i not in d1:
                if j in d2: return False
                else:
                    d1[i] = j
                    d2[j] = i
            elif d1[i] != j: return False
            
        return True