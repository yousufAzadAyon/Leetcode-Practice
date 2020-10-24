class Solution:
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        
        
        tokens.sort()
        print(tokens)
        
        score = 0
        ans = 0
        l = 0
        r = len(tokens) - 1
        while l <= r:
            if tokens[l] <= P:
                score += 1
                ans = max(ans, score)
                P -= tokens[l]
                l += 1
            else:
                if score >= 1:
                    score -= 1
                    P += tokens[r]
                    r -= 1
                else:
                    break
        return ans