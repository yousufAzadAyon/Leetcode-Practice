
        # week 2 day 1

class SolutionOne:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return 0
        return (n & (n-1)) == 0



        # week two day two

class SolutionTwo:
    def isSubsequence(self, s: str, t: str) -> bool:

        s_pointer = 0 
        t_pointer = 0
        
        while s_pointer < len(s) and t_pointer < len(t):
            if s[s_pointer] == t[t_pointer]:
                s_pointer += 1
                
            t_pointer += 1
            
        return s_pointer == len(s)


        # week two day three

class SolutionThree:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target > nums[len(nums) - 1]:
            return len(nums)
        
        for i in range(len(nums)):
            if nums[i] >= target:
                return i


        # week two day four 

class SolutionFour:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        start = 0
        end = len(nums)-1
        
        while i <= end:
            if nums[i] == 1:
                i+=1
            elif nums[i] == 0:
                if i == start:
                    i+=1
                else:
                    nums[start], nums[i] = nums[i], nums[start]
                start+=1
            else:
                nums[end], nums[i] = nums[i], nums[end]
                end-=1


        # using python builtin function 

class SolutionFourBuiltinFunction:
    def sortColors(self, nums):
        nums.sort()

        # easy but not efficient 


        # week two day five

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.list = []
        self.table = {}
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """

        if val in self.table:
            return False

        self.list.append(val)
        self.table[val] = len(self.list) - 1
        return True

        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.table:
            return False

        index = self.table[val]
        self.list[index] = self.list[-1]
        self.table[self.list[index]] = index
        self.list.pop()
        del self.table[val]
        
        
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.list)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()


            # week two day six

class SolutionFive:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        N = len(nums)
        if N == 0:
            return []
        
        prev = [-1] * N
        best = [1] * N
        
        for index, num in enumerate(nums):
            for pre_index in range(0, index):
                pre_num = nums[pre_index]
                if num % pre_num == 0:
                    if best[index] < best[pre_index] + 1:
                        best[index] = best[pre_index] + 1
                        prev[index] = pre_index
                        
        high = 0
        for index, num in enumerate(best):
            if best[index] > best[high]:
                high = index
                
        result = []
        
        while high != -1:
            result.append(nums[high])
            high = prev[high]
            
        return result 


            # week two day seven
            # 
class SolutionSeven:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        adj = collections.defaultdict(list)
        K += 1
        
        for u,v,w in flights:
            adj[u].append((v,w))
            
        seen = {}
        pq = []
        heapq.heappush(pq, (0,0,src))
        seen[(src, 0)] = 0
        
        while len(pq) > 0:
            dist, k, city = heapq.heappop(pq)
            
            if city == dst:
                return dist
            if seen[(city, k)] < dist:
                continue
                
            for v, w in adj[city]:
                if k + 1 <= K and ((v, k+1) not in seen or seen[(v, k+1)] > dist + w):
                    heapq.heappush(pq, (dist + w, k+1, v))
                    seen[(v, k+1)] = dist + w
                    
        return -1 

        