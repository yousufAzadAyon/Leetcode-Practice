class Solution:
    def postorderTraversal(self, root):
        self.res = []
        def postorder(root):
            if not root:
                return
            if root.left:
                postorder(root.left)
            if root.right:
                postorder(root.right)
            self.res.append(root.val)
        postorder(root)
        return self.res