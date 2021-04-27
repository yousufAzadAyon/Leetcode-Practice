class Solution:
    def hammingWeight(self, n):
        num_of_ones = 0

        for i in range(64):
            num_of_ones += (n&1)
            n = n>>1

        return num_of_ones