from itertools import accumulate
class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        dp = [0] * (k + 1)
        dp[0] = 1
        for i in range(1, n + 1):
            #print(dp)
            total = list(accumulate(dp))
            #print(total)
            new_dp = [0] * (k + 1)
            for j in range(k + 1):
                if j + 1 <= i:
                    new_dp[j] = total[j]
                else:
                    new_dp[j] = total[j] - total[j - i]
                if new_dp[j] == 0:
                    break
            dp = new_dp
        return dp[k] % (10 ** 9 + 7)