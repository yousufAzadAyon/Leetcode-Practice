class Solution:
    def runningSum(self, nums):
        temp = 0
        result = []
        for i in range(len(nums)):
            temp += nums[i]
            result.append(temp)
        return result

