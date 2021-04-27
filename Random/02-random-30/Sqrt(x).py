class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        if x == 1:
            return 1
        y = x
        for i in range(25):     # 25 iterations of Newton's method
            y = 0.5 * (y + x/y)
        return int(y)