class Solution:
    def openLock(self, deadends, target: str) -> int:
        up_bottom = {'0000'}
        bottom_up = {target}
        deadends = set(deadends)
        step = 0
        def increase(s,i):
            t = str(int(s[i]) + 1) if s[i] != '9' else'0'
            return s[:i] + t + s[i+1:]
        def decrease(s,i):
            t = str(int(s[i]) - 1) if s[i] != '0' else'9'
            return s[:i] + t + s[i+1:]
        while up_bottom and bottom_up:
            tmp = set()
            if len(up_bottom) <= len(bottom_up):
                for i in up_bottom:
                    if i in deadends:
                        continue
                    deadends.add(i)
                    if i in bottom_up:
                        return step
                    for j in range(4):
                        tmp.add(increase(i,j))
                        tmp.add(decrease(i,j))
                up_bottom = tmp
            else:
                for i in bottom_up:
                    if i in deadends:
                        continue
                    deadends.add(i)
                    if i in up_bottom:
                        return step

                    for j in range(4):
                        tmp.add(increase(i,j))
                        tmp.add(decrease(i,j))
                bottom_up = tmp
            step = step + 1
        return -1