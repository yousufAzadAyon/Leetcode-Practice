from collections import defaultdict, Counter
class Solution:
    def longestStrChain(self, words) -> int:
        words = sorted(words, key=lambda x: len(x))
        distances = {}
        
        for word in words:
            ans = 1
            for idx in range(len(word)):
                predecessor = word[:idx] + word[idx+1:]
                if predecessor in distances:
                    ans = max(ans, distances[predecessor]+1)
                
            distances[word] = ans
        return max(distances.values())