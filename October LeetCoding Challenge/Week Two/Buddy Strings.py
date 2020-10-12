class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False

        temp = []

        for i in range(len(A)):
            if A[i] != B[i]:
                temp.append(i)
        if len(temp) > 2:
            return False
        if len(temp) == 1:
            return False
        if len(temp) == 2:
            i, j = temp
            if A[i] == B[j] and B[i] == A[j]:
                return True
            else:
                return False
        if len(temp) == 0:
            if len(set(list(A))) < len(A):
                return True
            else:
                return False