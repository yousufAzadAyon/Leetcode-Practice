class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        
        def helper(cur, target, cur_sum, index):
            if target == cur_sum:
                res.append(cur)
            find = target - cur_sum
            for i in range(index, len(candidates)):
                a = candidates[i]
                if a > find:
                    break
                helper(cur+[a], target, cur_sum+a, i)
        
        helper([], target, 0, 0)
        return res