class Solution:
    def numDecodings(self, s: str) -> int:
        self.memo = {}
        return self.helper(s)

    def helper(self, s: str) -> int:
        if len(s) == 0: return 1
        if s in self.memo: return self.memo[s]
        
        takeOne = takeTwo = 0
        
        if int(s[:1]) >= 1 and int(s[:1]) <= 9:
            takeOne = self.helper(s[1:])
        
        if int(s[:2]) >= 10 and int(s[:2]) <= 26: 
            takeTwo = self.helper(s[2:])
        
        self.memo[s] = takeOne + takeTwo
        
        return self.memo[s]