class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num_to_alpha = {
            '2': list('abc'),
            '3': list('def'),
            '4': list('ghi'),
            '5': list('jkl'),
            '6': list('mno'),
            '7': list('pqrs'),
            '8': list('tuv'),
            '9': list('wxyz')
        }
        ans = []
        
        for num in digits:
            if ans:
                temp = []       
                for i in range(len(ans)):
                    for e in num_to_alpha[num]:
                        temp.append(ans[i] + e)
                ans = temp
            else:
                for e in num_to_alpha[num]:
                    ans.append(e)
     
        return ans