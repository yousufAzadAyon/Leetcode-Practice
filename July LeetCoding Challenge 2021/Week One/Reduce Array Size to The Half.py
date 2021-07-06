class Solution:
    def minSetSize(self, arr) -> int:
        cnt = {}
        for num in arr:
            if num not in cnt:
                cnt[num] = 1
            else:
                cnt[num] += 1
        cnt = list(cnt.values())
        cnt.sort(reverse=True)
        n = len(arr)
        curr = 0
        i = 0
        while curr*2 < n:
            curr += cnt[i]
            i += 1
        return i