class Solution:
    def __init__(self):
        self.res = []
        
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        if not s:
            return [""]
        wordDict = set(wordDict)
        dp = self.generateDP(s, wordDict)
        self.dfs(s, "", dp, 0, wordDict)
        return self.res
    
    def generateDP(self, s, word_dict):
        N = len(s)
        dp = [False] * (N+1)
        dp[0] =True
        for i in range(N):
            for j in range(i, N+1):
                if dp[i] and s[i:j] in word_dict:
                    dp[j] = True
        return dp
    
    def dfs(self, s, path, dp, ind, word_dict):
        print(path.strip())
        if dp[ind+len(s)]:
            if not s:
                self.res.append(path.strip())
            
            for i in range(1, len(s)+1):
                if s[:i] in word_dict:
                    self.dfs(s[i:], path+ " " + s[:i], dp, ind+i, word_dict)
                    