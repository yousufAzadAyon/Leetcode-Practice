class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        times = []
        def dfs(A = A, curr = []):
            if len(A) == 0:
                time = (10*curr[0]+curr[1], 10*curr[2]+curr[3])
                if time[0] < 24 and time[1] < 60:
                    times.append(time)
                return
            for i in range(len(A)):
                temp = A[:i] + A[i+1:]
                dfs(temp, curr + [A[i]])
        dfs()
        if len(times) == 0:
            return ""
        times.sort()
        biggest = times[-1]
        time = ""
        if biggest[0] == 0:
            time += "00"
        elif biggest[0] < 10:
            time += "0" + str(biggest[0])
        else:
            time += str(biggest[0])
        time += ":"
        if biggest[1] == 0:
            time += "00"
        elif biggest[1] < 10:
            time += "0" + str(biggest[1])
        else:
            time += str(biggest[1])
        return time