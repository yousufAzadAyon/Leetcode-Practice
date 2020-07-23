class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        seen = {}
        result = []
        for i in nums:
            if i not in seen:
                seen[i] = 1
                
            else:
                seen[i] += 1
                
        for i,j in seen.items():
            if j == 1:
                result.append(i)
                
        return result 