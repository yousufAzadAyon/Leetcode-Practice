class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_dict = {}
        for word in words:
            word_dict[word] = word_dict.get(word, 0) + 1
        word_len = len(words[0])
        
        i = 0
        res = []
        while i + word_len <= len(s):
            curr_dict = word_dict.copy()
            j = i
            while j + word_len <= len(s) and s[j:j+word_len] in curr_dict:
                curr_dict[s[j:j+word_len]] -= 1
                if curr_dict[s[j:j+word_len]] == 0:
                    del curr_dict[s[j:j+word_len]]
                j += word_len
            if not curr_dict:
                res.append(i)
            i += 1
        return res