class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word[0].isupper():
            if len(word)==1:
                return True
            else:
                if word[1].isupper():
                    for s in word[1:]:
                        if not s.isupper():
                            return False
                else:
                    for s in word[1:]:
                        if s.isupper():
                            return False
        else:
            for s in word[1:]:
                if s.isupper():
                    return False
                
        return True