from heapq import *
class Solution:
    def scheduleCourse(self, C) -> int:
        h = []
        
        C.sort(key = lambda x: x[1])
        # return 0
        time = 0;
        for c in C:
            
            if time + c[0] <= c[1]:
                heappush(h, -c[0])
                time += c[0]
            else:
                if h:
                    if -h[0] > c[0]:
                        time -= -heappop(h)
                        time += c[0]
                        heappush(h, -c[0])
            
        return len(h)
        