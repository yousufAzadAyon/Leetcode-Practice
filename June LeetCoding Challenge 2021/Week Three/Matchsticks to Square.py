from typing import List
class Solution:
    def makesquare(self, nums: List[int]) -> bool:
        if not nums: 
            return False
        tot = sum(nums) 
        if tot % 4: 
            return False
        side = int(tot/4) 
        res = set() 
        self.dfs(
            0, nums, [[],0], res, side
        )

        return len(res) == len(nums)

    def dfs(self, i, nums, path, res, side):
        """
        path[0] is array containing indexes of path, path[1] in sum of elements represented by indexes in path[0]
        """
        if len(res) == len(nums):
            return
        if path[1] == side:

            res.update(path[0])
            return
        if path[1] > side:
            return
        for x in range(i, len(nums)):
            if len(res)==len(nums):
                break
            self.dfs(
                x+1, nums, [path[0]+[x],path[1]+nums[x]], res, side
            )