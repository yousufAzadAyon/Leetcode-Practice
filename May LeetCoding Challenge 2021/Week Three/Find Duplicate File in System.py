class Solution:
    def findDuplicate(self, paths):
        ans = defaultdict(list)
        for path in paths:
            l = path.split()
            for i in range(1, len(l)):
                name, cont = l[i].split("(")
                ans[cont[:-1]].append(l[0] + "/" + name)
                
        return [i for i in ans.values() if len(i) > 1]