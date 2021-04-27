class Solution:
    def handleEdgeCases(self):
        for num in self.nums:
            if num == self.target:
                return True
        return False
            
    def _search(self, lo_idx: int, hi_idx: int) -> bool:
        if hi_idx < lo_idx:
            return False
        
        lo, hi = self.nums[lo_idx], self.nums[hi_idx]
        
        if self.target in [lo, hi]:
            return True
        
        if lo_idx == hi_idx or lo_idx + 1 == hi_idx:
            return False
            
        mid_idx = (hi_idx - lo_idx) // 2 + lo_idx
        mid = self.nums[mid_idx]
        
        if self.target == mid:
            return True
            
        if lo < mid:
            if self.target > lo and self.target < mid:
                return self._search(lo_idx, mid_idx)
            else:
                return self._search(mid_idx, hi_idx)
        if mid < hi:
            if self.target > mid and self.target < hi:
                return self._search(mid_idx, hi_idx)
            else:
                return self._search(lo_idx, mid_idx)
            
        return self._search(lo_idx + 1, mid_idx - 1) or self._search(mid_idx + 1, hi_idx - 1)

    def search(self, nums: List[int], target: int) -> bool:
        self.nums = nums
        self.target = target
        n = len(nums)
        if n < 3: return self.handleEdgeCases()
        return self._search(0, n - 1)