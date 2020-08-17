class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        if not candies:
            return []
        
        res = [0 for i in range(num_people)]
        i = 0
        c = 0
        while True:
            if i < num_people:
                if candies >= i+1+c:
                    res[i] += i+1+c
                    candies = candies -(i+1+c)
                    i += 1
                else:
                    res[i] += candies
                    break
            else:
                c += num_people
                i = 0
        return res
                   