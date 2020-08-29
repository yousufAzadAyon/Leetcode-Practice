class Solution:
	def pancakeSort(self, A: List[int]) -> List[int]:
		ans=[]
		for i in range(len(A),1,-1):
			temp=A.index(max(A[:i]))
			if temp==i-1:
				continue
			else:
				A=A[temp::-1]+A[temp+1:]
				ans.append(temp+1)
				A=A[i-1::-1]+A[i:]
				ans.append(i)
		return ans