class Solution:
    
    def minDistance(self, word1: str, word2: str) -> int:  
        L = []
        for i in range(len(word1)+1):
            L.append(i)
        
        
        for i in range(1,len(word2)+1):
            Temp = [i]
            for j in range(1,len(word1)+1):
                
                if word2[i-1] == word1[j-1]:
                    Temp.append(L[j-1])
                else:
                    Temp.append(min(L[j-1],Temp[-1],L[j])+1)
            L = Temp
            
        return L[-1]