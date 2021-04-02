class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        haystack_len = len(haystack)
        needle_len = len(needle)

        if needle == '':
            return 0
        

        for i in range(haystack_len - needle_len + 1):
            if haystack[i:i+len(needle)] == needle:
                return i
            
        return -1