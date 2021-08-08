class Solution:
    def levelOrder(self, root):
        if not root: return []
        Q, ans = deque([root]), []
        
        while Q:
            level = []
            for i in range(len(Q)):
                node = Q.popleft()
                for child in node.children:
                    Q.append(child)
                level += [node.val] 
            ans += [level]

        return ans