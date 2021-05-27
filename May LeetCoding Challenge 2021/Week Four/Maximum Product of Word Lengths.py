class Solution:
    def maxProduct(self, words: List[str]) -> int:
        bitmap = defaultdict(int)
        ans = 0
        for word in words:
            num = 0
            for letter in word:
                num |= (1 << (ord(letter) - ord('a')))
            bitmap[num] = max(bitmap[num], len(word))
        
        for x in bitmap:
            for y in bitmap:
                if x != y and (x & y == 0):
                    ans = max(ans, bitmap[x]*bitmap[y])
        return ans