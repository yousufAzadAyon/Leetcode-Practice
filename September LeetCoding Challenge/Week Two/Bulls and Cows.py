class Solution:
    def getHint(self, secret, guess):
        a=0
        b=0
        for i in range(len(guess)):
            if(secret[i]==guess[i]):
                a=a+1
        
        for i in range(len(guess)):
            if(guess[i] in secret):
                b=b+1
                secret=secret.replace(guess[i], 'A', 1)
                
        return f"{a}A{b-a}B"