class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums) -> TreeNode:
        def buildTree(nums):
            if not nums: return None
            middle_point = int(len(nums)/2)
            res = TreeNode(
                left = buildTree(nums[:middle_point]), 
                right = buildTree(nums[middle_point+1:]), 
                val = nums[middle_point]
            )
            
            return res
        
        return buildTree(nums)