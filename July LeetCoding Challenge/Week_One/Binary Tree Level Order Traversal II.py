# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res,data=[],[]
        if not root:return res
        stack=[]
        stack.append(root)
        nCount=1
        while stack:
            node=stack.pop(0)
            data+=[node.val]
            nCount-=1
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            if nCount==0:
                res=[data]+res
                data=[]
                nCount=len(stack)
        return res