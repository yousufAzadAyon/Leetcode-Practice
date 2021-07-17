class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        countOnes = 0
        for num in arr:
            if num == 1:
                countOnes += 1
        if countOnes == 0:
            return [0, len(arr)-1]
        if countOnes % 3 != 0:
            return [-1, -1]
        
        k = countOnes // 3
        first = 0
        for i in range(len(arr)):
            if arr[i] == 1:
                first = i
                break
        second = -1
        count1s = 0
        for i in range(len(arr)):
            if arr[i] == 1:
                count1s += 1
            if count1s == k+1:
                second = i
                break
        third = -1
        count1s = 0
        for i in range(len(arr)):
            if arr[i] == 1:
                count1s += 1
            if count1s == 2*k+1:
                third = i
                break
        
        while third < len(arr):
            if arr[first] == arr[second] and arr[second] == arr[third]:
                first += 1
                second += 1
                third += 1
            else:
                break
        if third != len(arr):
            return [-1, -1]
        return [first-1, second]