from collections import Counter
import heapq

class Solution(object):
    def topKFrequent(self, nums, k):
        d, h = [(freq, num) for num, freq in Counter(nums).items()], []
        for i in range(k):
            heapq.heappush(h, d[i])
        for i in range(k, len(d)):
            if d[i][0] > h[0][0]:
                heapq.heappop(h)
                heapq.heappush(h, d[i])
        return [heapq.heappop(h)[1] for _ in range(k)][::-1]