# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        def dfs(root , level):
            if not root:
                return
            if level > len(queue) - 1:
                queue.append(deque([]))
            if not level & 1:
                queue[level].append(root.val)
            else:
                queue[level].appendleft(root.val)
            dfs(root.left , level + 1)
            dfs(root.right , level + 1)
            
        queue = []
        dfs(root , 0)

        return queue