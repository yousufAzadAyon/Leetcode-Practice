class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        res = ""

        def dfs(root):
            nonlocal res
            if not root:
                res += "None,"
                return
            res += str(root.val)+","
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return res

    def deserialize(self, data):
        idx = 0
        lst_data = data.split(',')[:-1]

        def dfs():
            nonlocal idx
            if lst_data[idx] == "None":
                return None
            node = TreeNode(int(lst_data[idx]))
            idx += 1
            node.left = dfs()
            idx += 1
            node.right = dfs()
            return node
        return dfs()
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))