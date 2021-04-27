class Solution:
    def maximalRectangle(self, matrix) -> int:
        if not matrix:
            return 0
        rows, cols, res = len(matrix), len(matrix[0]), 0
        for row in range(rows):
            for col in range(cols):
                matrix[row][col] = int(matrix[row][col])
                if row >= 1 and matrix[row][col] == 1:
                    matrix[row][col] = matrix[row-1][col] + 1
            res = max(res,self.max_histogram_area(matrix[row]))
        return res
    
    def max_histogram_area(self,height):
        stack, area,size = [], 0, len(height)
        for i in range(size):
            while stack and height[stack[-1]] > height[i]:
                h = height[stack.pop()]
                w = i if not stack else i - stack[-1] -1
                area = max(area, h*w)
            stack.append(i)
        while stack:
            h = height[stack.pop()]
            w = size if not stack else size - stack[-1] - 1
            area = max(area, h*w)
        return area