class Solution:
    def intToRoman(self, num):
        val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        roman = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]

        res = ''

        for i, v in enumerate(val):
            res += (num//v) * roman[i]
            num %= v

        return res
        
