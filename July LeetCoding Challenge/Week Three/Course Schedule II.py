from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # corner case
        if numCourses == 0:
            return []
        
        self.graph = [[] for _ in range(numCourses)]
        self.indegree = [0] * numCourses
        
        # construct graph
        for to_node, from_node in prerequisites:
            self.graph[from_node].append(to_node)
            self.indegree[to_node] += 1
            
        # topo sort
        queue = []
        schedule = []
        
        for node in range(numCourses):
            if self.indegree[node] == 0:
                queue.append(node)
                
        while queue:
            from_node = queue.pop()
            schedule.append(from_node)
            
            for to_node in self.graph[from_node]:
                self.indegree[to_node] -= 1
                if self.indegree[to_node] == 0:
                    queue.append(to_node)
        
        if len(schedule) == numCourses:
            return schedule
        return []