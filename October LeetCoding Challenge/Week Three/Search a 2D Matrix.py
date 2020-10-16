class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        heads = [row[0] for row in matrix]
        l, r = 0, len(heads)
        while l < r:
            m = (r+l)//2
            if heads[m] > target:
                r = m
            else:
                l = m + 1
        
        search_row = matrix[l-1]
        left, right = 0, len(search_row)
        while left < right:
            mid = (left+right)//2
            if search_row[mid] == target:
                return True
            elif search_row[mid] > target:
                right = mid
            else:
                left = mid + 1
        return False