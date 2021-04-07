class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        int_1 = self.get_integer(num1)
        int_2 = self.get_integer(num2)
        return str(int_1 * int_2)
    
    def get_integer(self, num_str: str) -> int:
        to_int = 0
        for idx in range(len(num_str) - 1, -1, -1):
            num = int(num_str[idx])
            multiplier = 10 ** (len(num_str) - 1 - idx)
            to_int += num * multiplier
        return to_int