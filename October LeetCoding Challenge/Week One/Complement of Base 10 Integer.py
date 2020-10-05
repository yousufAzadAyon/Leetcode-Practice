class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n==0:
            return 1
        ans=0
        count=0
        while n>0:
            if n%2==0:
                ans+=2**count
            n=n//2
            count+=1
            
        return ans