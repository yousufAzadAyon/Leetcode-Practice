        # week four day one

class SolutionOne:
    def singleNumber(self, nums: List[int]) -> int:
        seen = {}
        for i in nums:
            if i not in seen:
                seen[i] = 1
            else:
                seen[i] += 1
                
        for i,j in seen.items():
            if j != 3:
                return i

        # week four day two

class SolutionTwo:
    def countNodes(self, root: TreeNode) -> int:
        if root is None: return 0
        
        def rec(node, count):
            if node.left is not None:
                count = rec(node.left,count+1)
            if node.right is not None:
                count = rec(node.right,count+1)
            return count
        
        n_nodes = rec(root, 1)
        
        return n_nodes