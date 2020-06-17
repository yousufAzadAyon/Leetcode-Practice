        # week three day One

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        curr = root 
        while curr != None:
            if curr.val == val:
                return curr
            if curr.val > val:
                curr = curr.left
            else:
                curr = curr.right
                
        return curr

        

        # week three day two

class SolutionTwo:
    def validIPAddress(self, IP: str) -> str:
        res = 0
        ipv4 = IP.split('.')
        if len(ipv4) == 4:
            for x in ipv4:
                if x == '' or (x[0] == '0' and len(x) != 1) or not x.isdigit() or int(x) > 255:
                    res = 1
                    break
            if not res:
                return 'IPv4'
        
        ipv6 = IP.split(':')
        if len(ipv6) == 8:
            for x in ipv6:
                if x == '' or len(x) > 4 or not all(c in hexdigits for c in x):
                    res = 1
                    break
            if not res:
                return 'IPv6'
        
        return 'Neither'
        

        # week three day three

class SolutionThree:
    def mark_border(self, i, j, board):
        if i==-1 or i==len(board):
            return
        if j==-1 or j==len(board[0]):
            return
        if board[i][j]=='O':
            board[i][j]=''
            self.mark_border(i-1, j, board)
            self.mark_border(i+1, j, board)
            self.mark_border(i, j-1, board)
            self.mark_border(i, j+1, board)
        
    
    def solve(self, board):
        if not board or not board[0]:
            return []
        
        M, N = len(board), len(board[0])
        for i in range(M):
            self.mark_border(i, 0, board)
            self.mark_border(i, N-1, board)
        for j in range(N):
            self.mark_border(0, j, board)
            self.mark_border(M-1, j, board)
        
        for i in range(M):
            for j in range(N):
                if board[i][j]=='':
                    board[i][j]='O'
                elif board[i][j]=='O':
                    board[i][j]='X'