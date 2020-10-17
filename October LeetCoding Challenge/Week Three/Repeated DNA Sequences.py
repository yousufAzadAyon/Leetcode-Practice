class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 10:
            return []
        if len(s) == 10:
            return []
        d = {}
        ans = []
        for i in range(len(s) - 9):
            key = s[i:i + 10]
            if key in d:
                d[key] += 1
                if d[key] == 2:
                    ans.append(key)
            else:
                d[key] = 1
        return ans