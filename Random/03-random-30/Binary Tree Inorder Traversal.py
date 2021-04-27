class Solution:
    def inorderTraversal(self, root):
        out=[]
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            out.append(node.val)
            inorder(node.right)
            return
        inorder(root)
        return out
