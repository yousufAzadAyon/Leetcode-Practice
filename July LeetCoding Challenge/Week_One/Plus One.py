class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        temp = 0
        result = []
        for digit in digits:
            temp = (temp * 10) + digit
        final = temp + 1
        
        while final > 0:
            mod = final % 10
            result.append(mod)
            final //= 10
            
        return result[::-1]