class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = ""
        carry = 0
        i = len(a) - 1
        j = len(b) - 1
        
        while i >= 0 or j >= 0:
            a_count = 1 if i >= 0 and a[i] == "1" else 0
            b_count = 1 if j >= 0 and b[j] == "1" else 0
            
            (times, rem) = divmod(a_count + b_count + carry, 2)
            carry = times
            result = ("1" if rem else "0") + result
            
            i -= 1
            j -= 1
            
        result = "1" + result if carry else result
        
        return result