class Node:
    def __init__(self, val=0, left=None, right=None, next=None) -> None:
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root):
        if root:
            temp=[root]
            while True:
                if not temp[0].left:
                    break
                temp2=[]
                for e in temp:
                    temp2.extend([e.left,e.right])
                L=len(temp2)
                for l in range(L-1):
                    temp2[l].next=temp2[l+1]
                temp=temp2
        return root