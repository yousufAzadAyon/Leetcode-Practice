class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        MAGIC = 10**5
        L, R = int(left), int(right)
        count = 0
        
        def valid(num):
            return str(num) == str(num)[::-1]

        for k in range(MAGIC):
            string = str(k)
            odd = int(string[:-1] + string[::-1])
            v = odd * odd
            if v < L:
                continue
            if v > R:
                break
            count += valid(v)
        
        for k in range(MAGIC):
            string = str(k)
            even = int(string + string[::-1])
            v = even * even
            if v < L:
                continue
            if v > R:
                break
            count += valid(v)
        
        return count
