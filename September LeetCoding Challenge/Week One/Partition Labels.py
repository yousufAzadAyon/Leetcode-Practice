class Solution(object):
    def partitionLabels(self, S):
        if not S:
            return []

        res = []
        start = 0
        end = S.rfind(S[0])
        i = 0
        n = len(S)
        while i < n-1:
            if i == end:
                res.append(end-start+1)
                start = i + 1
                end = S.rfind(S[i+1])
            else:
                end = max(end, S.rfind(S[i]))
            i += 1
        res.append(end-start+1)
        return res