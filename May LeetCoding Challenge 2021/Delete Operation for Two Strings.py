class Solution:
	def minDistance(self, a: str, b: str) -> int:
		n = len(a)
		m = len(b)

		if n == 0 or m == 0:
			return max(n,m)
		if n == 0 and m == 0:
			return 0
		if n == 1 and m == 1:
			if a[0] == b[0]:
				return 0
			else:
				return 2
		dp = [[0 for x in range(m + 1)] for y in range(n + 1)]

		for i in range(1, n + 1):
			for j in range(1, m + 1):
				if a[i - 1] == b[j - 1]:
					dp[i][j] = 1 + dp[i - 1][j - 1]
				else:
					dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

		return n + m - (2 * dp[-1][-1])