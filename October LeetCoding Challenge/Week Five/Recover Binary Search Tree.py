class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        def morrisInOrder(root):
            while root:
                if not root.left:
                    yield root
                    root = root.right
                else:    
                    prev = root.left
                    while prev.right and prev.right != root:
                        prev = prev.right
                    if not prev.right:
                        prev.right = root
                        root = root.left
                    else:
                        yield root
                        prev.right = None
                        root = root.right
        prev, first, second = None, None, None
        for curr in morrisInOrder(root):
            if prev and prev.val > curr.val:
                if not first:
                    first = prev
                second = curr
            prev = curr
        first.val, second.val = second.val, first.val 