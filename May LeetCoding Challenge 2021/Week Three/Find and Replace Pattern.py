class Solution:
    def findAndReplacePattern(self, words, pattern: str):
        results = []
        for word in words:
            d1 = {}
            d2 = {}
            found = True
            for i in range(len(pattern)):
                if pattern[i] in d1 or word[i] in d2:
                    if word[i] != d1.get(pattern[i]) or d2.get(word[i]) != pattern[i]:
                        found = False
                        break
                else:
                    d1[pattern[i]] = word[i]
                    d2[word[i]] = pattern[i]
            if found:
                results.append(word)
        
        return results