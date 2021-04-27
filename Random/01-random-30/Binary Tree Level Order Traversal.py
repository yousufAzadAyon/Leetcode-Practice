class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root):
        if not root:
            return 
        else:
            s1 = []
            res = []
            s1.append(root)
            
            while len(s1)>0:
                l=[]
                for i in range(len(s1)):
                    temp = s1.pop(0)
                    l.append(temp.val)
                    if temp.left:
                        s1.append(temp.left)
                    if temp.right:
                        s1.append(temp.right)
                res.append(l)
            return res