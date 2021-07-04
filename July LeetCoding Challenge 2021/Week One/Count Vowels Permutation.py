class Solution:
    def countVowelPermutation(self, n):
        mod=10**9+7
        a=e=i=o=u=1
        for _ in range(n-1):
            a,e,i,o,u=(e+i+u)%mod,(a+i)%mod,(e+o)%mod,i,(i+o)%mod
        return (a+e+i+o+u)%mod