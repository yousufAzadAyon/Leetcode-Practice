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



            # week three day four

class SolutionFour:
    def hIndex(self, citations):
        if not citations: return 0
        n = len(citations)
        beg, end = 0, n - 1
        while beg <= end:
            mid = (beg + end)//2
            if mid + citations[mid] >= n:
                end = mid - 1
            else:
                beg = mid + 1
        return n - beg

            # week three day five

class SolutionFive:
    def RabinKarp(self,text, M, q):
        if M == 0: return True
        h,t,d = 1,0,256

        dic = defaultdict(list)
        for i in range(M-1):  h = (h * d) % q 

        for i in range(M): 
            t = (d * t + ord(text[i]))% q

        dic[t].append(i-M+1)

        for i in range(len(text) - M):
            t = (d*(t-ord(text[i])*h) + ord(text[i + M]))% q
            dic[t].append(i+1)

        for key in dic:
            for i,j in combinations(dic[key], 2):
                if text[i:i+M] == text[j:j+M]:
                    return (True, text[i:i+M])

        return (False, "")


    def longestDupSubstring(self, S):
        beg, end = 0, len(S)
        q = (1<<31) - 1 
        Found = ""
        while beg + 1 < end:
            mid = (beg + end)//2
            isFound, candidate = self.RabinKarp(S, mid, q)
            if isFound:
                beg, Found = mid, candidate
            else:
                end = mid

        return Found


        # week three day six

class SolutionSix:
    def getPermutation(self, n: int, k: int) -> str:
        fact = [1]
        num = [1]
        i=1;
        while(i < n):
            num.append(i+1)
            a  = fact.pop(len(fact)-1)
            fact.append(a)
            fact.append(a*i)
            i+=1
        i=1
        str_n = 0
        k-=1
        while(i <= n):
            index = int((k)/fact[n-i])
            str_n = 10*str_n + num[index]
            num.remove(num[index])
            k %=fact[n-i]
            i+=1
        return str(str_n)

            # week three day seven

class SolutionSeven:
    def calculateMinimumHP(self, dungeon):
        m, n = len(dungeon), len(dungeon[0])
        dp = [[0]*(n+1) for _ in range(m+1)]
        
        dp[m-1][n], dp[m][n-1] = 1, 1
        for i in range(m-1): dp[i][n] = float("inf")
        for j in range(n-1): dp[m][j] = float("inf")
            
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                dp[i][j] = max(min(dp[i+1][j],dp[i][j+1])-dungeon[i][j],1)
        
        return dp[0][0]

        