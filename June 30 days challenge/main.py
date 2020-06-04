#%%
# day one
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class SolutionOne:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root:
            left = self.invertTree(root.right)
            right = self.invertTree(root.left)
            root.left = left
            root.right = right 
        return root

# day two 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class SolutionTwo:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        :Stupid Question
        """
        node.val = node.next.val
        node.next = node.next.next


# Day Three

class SolutionThree:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        sorted_cost = sorted(costs, key= lambda x:x[0] - x[1])
        result = 0
        
        for i in range(len(costs)):
            if i < len(costs)/2:
                result += sorted_cost[i][0]
                
            else:
                result += sorted_cost[i][1]
                
        return result


    # Day Four

class Solution:
    def reverseString(self, s: List[str]) -> None:
        s.reverse()
        """
        Do not return anything, modify s in-place instead.
        """
        
        # without build in function

        # def reverseStringWithoutFunction(s):
        #     i = 0 
        #     j = len(s) - 1 

        #     while i<j:
        #         s[i], s[j] = s[j], s[i]
        #         i += 1
        #         j -= 1

