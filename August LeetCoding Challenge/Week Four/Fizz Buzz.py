class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        temp = []
        for num in range(1, n+1):
            if num % 3 == 0 and num % 5 == 0:
                temp.append('FizzBuzz')
            elif num % 3 == 0:
                temp.append('Fizz')
            elif num % 5 == 0:
                temp.append('Buzz')
                
            else:
                temp.append(str(num))
        return temp