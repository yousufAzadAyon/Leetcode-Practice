class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        ans=[]
        z=""
        for ch in searchWord:
            temp=[]
            z+=ch
            index=self.binary_search(products,z)
            for i in range(index,min(index+3,len(products))):
                if products[i].startswith(z):
                    temp.append(products[i])
            ans.append(temp)
        return ans
    def binary_search(self,A,s):
        lo=0
        hi=len(A)
        while lo<hi:
            mid=(lo+hi)//2
            if A[mid]<s:
                lo=mid+1
            else:
                hi=mid
        return lo