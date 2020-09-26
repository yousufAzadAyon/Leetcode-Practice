class Solution:
	def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
		if not timeSeries:
			return 0
		if len(timeSeries)==1:
			return duration
		timeSeries=sorted(timeSeries)
		res=0
		for i in range(1,len(timeSeries)):
			if timeSeries[i]-timeSeries[i-1]<duration:
				res+=timeSeries[i]-timeSeries[i-1]
			else:
				res+=duration
		res+=duration
		return res