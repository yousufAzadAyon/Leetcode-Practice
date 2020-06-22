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

