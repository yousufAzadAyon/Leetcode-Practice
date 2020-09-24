class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        seen = {}
        for i in s:
            if i not in seen:
                seen[i] = 1
            else:
                seen[i] += 1
                
        for i in t:
            if i not in seen:
                seen[i] = 1
            else:
                seen[i] -= 1
                
        for i,j in seen.items():
            if j != 0:
                return i
