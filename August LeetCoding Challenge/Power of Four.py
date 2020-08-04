class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num <=0: return False
        cnt,i = 0,0
        while num:
            if num & 1:
                cnt += 1
                if cnt > 1 or i %2 == 1:
                    return False
            num,i = num >> 1, i + 1
        return True