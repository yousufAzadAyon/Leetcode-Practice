class Solution:
    def trap(self, H):
        left = list(accumulate(H, max))
        right = list(accumulate(H[::-1], max))[::-1]
        return sum(min(i, j) - k for i, j, k in zip(left, right, H))