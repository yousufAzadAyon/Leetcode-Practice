class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        
        lastIndex = {a:i for i, a in enumerate(s)}
        res = []
        
        for i, a, in enumerate(s):
            if a in res:
                continue
            
            while res and res[-1] > a and i < lastIndex[res[-1]]:
                res.pop()
            res.append(a)
            
        return "".join(res)