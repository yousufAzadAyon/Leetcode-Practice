from typing import List
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.n = int(len(nums) ** 0.5) + 1
        self.sums = [sum(self.nums[i*self.n:i*self.n + self.n]) for i in range(self.n)]
        

    def update(self, index: int, val: int) -> None:
        self.sums[index // self.n] += val - self.nums[index]
        self.nums[index] = val

    def sumRange(self, left: int, right: int) -> int:
        left_start = left // self.n
        right_start = right // self.n
        sums = sum(self.sums[left_start:right_start+1])
        
        sub = sum(self.nums[left_start*self.n:left]) + sum(self.nums[right+1:(right_start+1)*(self.n)])

        return sums - sub

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)