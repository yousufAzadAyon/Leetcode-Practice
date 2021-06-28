class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        
        for c in s:
            if stack:
                last = stack[-1]
                if c == last:
                    stack.pop()
                else:
                    stack.append(c)
            else:
                stack.append(c)
        
        return "".join(stack)