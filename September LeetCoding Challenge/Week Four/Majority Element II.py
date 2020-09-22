class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        result=[]
        num1,num2,c1,c2=-1,-1,0,0
        for n in nums:
            if n==num1:
                c1+=1
            elif n==num2:
                c2+=1
            elif c1==0:
                num1=n
                c1+=1
            elif c2==0:
                num2=n
                c2+=1
            else:
                c1-=1
                c2-=1
        for j in [num1,num2]:
            if nums.count(j)>len(nums)//3:
                result.append(j)
        return result