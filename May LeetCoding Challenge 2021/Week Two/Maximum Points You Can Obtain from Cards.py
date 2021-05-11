class Solution:
    def maxScore(self, cardPoints, k: int) -> int:
        sum_l = sum(cardPoints[:k])
        res = sum_l
        for i in range(k):
            sum_l += -cardPoints[k - i - 1] + cardPoints[-i-1]
            res = max(res, sum_l)

        return res