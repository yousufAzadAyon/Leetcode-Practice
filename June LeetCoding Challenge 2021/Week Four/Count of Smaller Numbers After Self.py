from typing import List
from collections import deque
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        lst = deque()
        
        for item in range(len(nums) - 1, -1, -1):
            val = nums[item]
            if not lst or val > lst[len(lst) - 1]:
                nums[item] = 0 if not lst else len(lst)
                lst.append(val)
            else:
                i, j = 0, len(lst) - 1
                while i <= j:
                    mid = i + (j - i) // 2

                    if lst[mid] < val:
                        i = mid + 1
                    if lst[mid] >= val:
                        j = mid - 1
        
                nums[item] = i
                lst.insert(i, val)
        
        return nums