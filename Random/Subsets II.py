class Solution:
    def combinationSum(self, candidates, target: int):
        if not candidates: return []
        res = []
        candidates.sort()
        def dfs(idx, path, cur):
            if cur > target: return
            if cur == target:
                res.append(path)
                return
            for i in range(idx, len(candidates)):
                dfs(i, path+[candidates[i]], cur+candidates[i])
        dfs(0, [], 0)
        return res