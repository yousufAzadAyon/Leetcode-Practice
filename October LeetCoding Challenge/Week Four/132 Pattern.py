class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        n = len(nums)
        minimum = nums[0]
        stack = [(nums[0], nums[0])]
        for i in range(1,n):
            if nums[i] < minimum:
                minimum = nums[i]
            else:
                while stack and nums[i] > stack[-1][0]:
                    if stack[-1][1] > nums[i]:
                        return True
                    else:
                        stack.pop()
            stack.append((minimum, nums[i]))
        return False