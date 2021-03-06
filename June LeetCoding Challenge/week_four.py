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

        # week four day three

class SolutionThree:
    def numTrees(self, n: int) -> int:
		# Base case:
		# 0 nodes = 1 tree
        # 1 nodes = 1 tree
		
        # numTree[4] = numTree[0] * numTree[3] +
        #              numTree[1] * numTree[2] +
        #              numTree[2] * numTree[1] +
        #              numTree[3] * numTree[0]
		
        numTree = [1] * (n + 1)
        for nodes in range(2, n + 1):
            total = 0
            for root in range(1, nodes + 1):
                left = root - 1
                right = nodes - root
                total += numTree[left] * numTree[right]
            numTree[nodes] = total
        return numTree[n]

        # week four day four

class SolutionFour:
    def findDuplicate(self, nums: List[int]) -> int:
        sor = sorted(nums)
        for i in sor:
            if sor[i] == sor[i-1]:
                return sor[i]

        # week four day five

class SolutionFive:
    def sumNumbers(self, root):
        if not root: return 0
        
        if not root.left and not root.right:
            return int(root.val)
        
        if root.left: root.left.val = 10*root.val + root.left.val
        if root.right: root.right.val = 10*root.val + root.right.val
            
        return self.sumNumbers(root.left) + self.sumNumbers(root.right)


        # week four day six

class SolutionSix:
    def numSquares(self, n: int) -> int:
        arr, i = [], 1
        while i**2 <= n:
            arr.append(i**2)
            i += 1
        
        #one-sum O(N^(1/2))
        if n in arr:
            return 1
        
        #two-sum O(N)
        for e in arr:
            if n-e in arr:
                return 2
        
        #three-sum O(N)
        arr_set = set(arr)
        for i in range(len(arr)):
            for j in range(len(arr)):
                if n-arr[i]-arr[j] in arr_set:
                    return 3
        
        #four-sum O(1)
        return 4

        # week four day seven 

class SolutionSeven:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        def dfs(dep):
            arr = paths[dep]
            while arr:
                dfs(arr.pop())
            res.append(dep)

        res = []
        paths = defaultdict(list)
        tickets.sort(key=lambda x: x[1], reverse=True)
        for s, t in tickets:
            paths[s].append(t)
        dfs('JFK')
        return res[::-1]

