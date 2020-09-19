class Solution:
    def sequentialDigits(self, low, high):
        answer=[]
        for i in range(1,10):
            number=i
            next=i
            while(number<=high and next<10):
                if number>=low:
                    answer.append(number)
                next=next+1
                number=number*10+next
        return sorted(answer)