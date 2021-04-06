class Solution:
    
    def inc_bs(self,arr, target):
        low = 0
        high = len(arr)-1
        while low<=high:
            mid = low+(high-low)//2
            if arr[mid]==target:
                return mid
            elif arr[mid]>target:
                high=mid-1
            else:
                low=mid+1
        return None
    
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1
        n = len(nums)
        pivot = 0
        if len(nums)<=1:
            return 0 if nums and nums[0]==target else -1
        start = nums[0]
        while low<=high:
            mid = low+(high-low)//2
            prev = (n+(mid-1))%n
            nxt = (mid+1)%n
            if nums[mid]<nums[nxt] and nums[mid]<nums[prev]:
                pivot = mid
                break
            elif start<=nums[mid]:
                low=mid+1
            elif start>nums[mid]:
                high=mid-1
        ele = self.inc_bs(nums[pivot:], target)
        if ele!=None:
            return pivot+ele
        ele = self.inc_bs(nums[:pivot], target)
        if ele!=None:
            return ele
        return -1