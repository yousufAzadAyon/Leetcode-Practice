class Solution(object):
    def minMoves2(self, nums):
        n = len (nums)
        mid = sorted (nums) [n // 2]
        res = sum (abs (i - mid) for i in nums)
        return res