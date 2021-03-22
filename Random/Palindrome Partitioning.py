class Solution:
    def dfs(self, s, partition, result):
        if not s:
            result.append(partition[::])
            return

        for i in range(1, len(s)+1):
            prefix, postfix = s[:i], s[i:]
            if self.is_palindrome(prefix):
                partition.append(prefix)
                self.dfs(postfix, partition, result)
                partition.pop()

    def is_palindrome(self, s):
        return s == s[::-1]

    def partition(self, s):
        result = []

        self.dfs(s, [], result)
        return result