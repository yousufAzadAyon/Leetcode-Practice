class Solution:
    def arrangeCoins(self, n: int) -> int:
        l, r = 1, 65536
        while l < r:
            mid = (l + r) >> 1
            if mid * (mid + 1) // 2 <= n:
                l = mid + 1
            else:
                r = mid
        return l - 1


#         simple solution 

# class Solution(object):
#     def arrangeCoins(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         k = 1
        
#         while n >= 0:
#             n -= k
#             k += 1
            
#         return k - 2