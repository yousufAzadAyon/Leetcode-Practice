class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        char_freq = sorted(Counter(tasks).values() , reverse = True)
        index , counter , max_freq = 0 , 0 , char_freq[0]
        while index < len(char_freq) and char_freq[index] == max_freq:
            counter += 1
            result = (max_freq - 1) * (n + 1) + counter
            index += 1
        return max(result , len(tasks))