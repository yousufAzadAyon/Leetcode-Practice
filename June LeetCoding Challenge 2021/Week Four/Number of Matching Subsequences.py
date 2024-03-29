class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        i = 0
        final_count = Counter(words)
        
        for word in set(words):
            it = iter(s)
            if all(letter in it for letter in word):
                i += final_count[word]
        
        return i