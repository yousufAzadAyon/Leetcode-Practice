class Solution(object):
    def numSubarrayBoundedMax(self, A, L, R):
        """
        :type A: List[int]
        :type L: int
        :type R: int
        :rtype: int
        """
        res, dp = 0, 0
        prev = -1
        for i in range(len(A)):
            if A[i] < L and i > 0:
                res += dp
            if A[i] > R:
                dp = 0
                prev = i
            if L <= A[i] <= R:
                dp = i - prev
                res += dp
        return res