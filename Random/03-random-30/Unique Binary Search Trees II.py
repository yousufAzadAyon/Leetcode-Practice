# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def generateTrees(self, n: int):
        
        if n == 0:
            return []
        
        def helper(start,end):  # my helper function 
            
            if start > end:  # when we reach at the leaf node
                return [None]
            
            res = []                    # for each tree 
            
            for i in range(start,end+1):
                
                left = helper(start,i-1) 
                right = helper(i+1,end)   
                
                for l in left:            # iterating over left nodes of the root node
                    for r in right:        # iterating over right nodes of the root node            
                        node = TreeNode(i)  # creating a node 
                        node.left = l       # constructing left side
                        node.right = r      # constructing right side
                        res.append(node)  
            print(res)
            return res
        
        return helper(1,n)