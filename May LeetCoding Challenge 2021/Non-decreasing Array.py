class Solution:
    def checkPossibility(self, nums):
        if len(nums) == 1 or len(nums) == 2:
            return True
        count, diff = 0, []
        for i in range(len(nums)-1):
            diff.append(nums[i+1] - nums[i])
            if nums[i] > nums[i+1]:
                count += 1
                if count > 1:
                    return False
        if len(diff)>2:
            for j in range(len(diff)-1):
                if ((diff[j+1] + diff[j]) < 0) and (j < len(diff)-2):
                    if (diff[j+2] + diff[j+1]) < 0:
                        return False
        return True