class UnionFind(object):
    
    def __init__(self, n):  
        self.data = [i for i in range(n)]
        self.group_size = [1] * n
        self.size = n
        
    def find(self, x):  
        if x != self.data[x]:
            self.data[x] = self.find(self.data[x])
        return self.data[x]

    def union(self, x, y):  
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root == y_root:
            return
        self.data[x_root] = y_root
        self.group_size[y_root] += self.group_size[x_root]
        self.group_size[x_root] = 0
        self.size -= 1
        
class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        
        def primefactors(n):
            factors = set()
            while n % 2 == 0:
                n = n // 2
                factors.add(2)
                
            for i in range(3, int(math.sqrt(n)) + 1, 2):
                while n % i == 0:
                    factors.add(i)
                    n = n // i
            
            if n > 2:
                factors.add(n)
            return factors
        
        N = len(A)
        uf = UnionFind(N)
        factor_to_index = dict()
        
        for idx, n in enumerate(A):
            factors = primefactors(n)
            for factor in factors:
                if factor in factor_to_index:
                    uf.union(idx, factor_to_index[factor])
                factor_to_index[factor] = idx
        
        return max(uf.group_size)