class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        table = [False] * len(s)
        for i in range(len(table)):
            if s[0:i+1] in wordSet:
                table[i] = True
            else:
                for j in range(0,i):
                    if table[j] == True:
                        if s[j+1:i+1] in wordSet:
                            table[i] = True
                            break
        
        return table[-1]