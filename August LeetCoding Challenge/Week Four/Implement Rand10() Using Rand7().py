# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        while (True):
            a = rand7()
            b = rand7()
            idx = b + 7 * (a - 1)
            if (idx <= 40):
                return 1 + (idx - 1) % 10
            a = idx - 40
            b = rand7()
            idx = b + (a - 1) * 7
            if (idx <= 60):
                return 1 + (idx - 1) % 10
            a = idx - 60
            b = rand7()
            idx = b + (a - 1) * 7
            if (idx <= 20):
                return 1 + (idx - 1) % 10