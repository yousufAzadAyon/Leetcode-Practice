#%%
# day one
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class SolutionOne:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root:
            left = self.invertTree(root.right)
            right = self.invertTree(root.left)
            root.left = left
            root.right = right 
        return root

# day two 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class SolutionTwo:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        :Stupid Question
        """
        node.val = node.next.val
        node.next = node.next.next


# Day Three

class SolutionThree:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        sorted_cost = sorted(costs, key= lambda x:x[0] - x[1])
        result = 0
        
        for i in range(len(costs)):
            if i < len(costs)/2:
                result += sorted_cost[i][0]
                
            else:
                result += sorted_cost[i][1]
                
        return result


    # Day Four

class Solution:
    def reverseString(self, s: List[str]) -> None:
        s.reverse()
        """
        Do not return anything, modify s in-place instead.
        """
        
        # without build in function

        # def reverseStringWithoutFunction(s):
        #     i = 0 
        #     j = len(s) - 1 

        #     while i<j:
        #         s[i], s[j] = s[j], s[i]
        #         i += 1
        #         j -= 1

        # day five

class SolutionFive:

    def __init__(self, w: List[int]):
        self.w = []
        total = 0
        for weight in w:
            total += weight
            self.w.append(total)
        self.total = total 
        

    def pickIndex(self) -> int:
        #from random import random

        random_number = self.total * random.random()      #works without import
        low, high = 0, len(self.w)
        while low < high: 
            mid = low + (high - low) // 2
            if random_number > self.w[mid]:
                low = mid + 1 
            else:
                high = mid
                
        return low

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()

        # day six

class SolutionSix:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key= lambda x:(x[1], x[0]) )
        
        
        result = []
        for height, number in people:
            if len(result) == 0:
                result. append((height, number))
                continue 
                
            count = 0
            for index, (qheight, qnumber) in enumerate(result):
                if qheight >= height:
                    count += 1
                if count > number:
                    result.insert(index, (height, number))
                    break
                    
            else:
                result.append((height,number))
                
        return result

