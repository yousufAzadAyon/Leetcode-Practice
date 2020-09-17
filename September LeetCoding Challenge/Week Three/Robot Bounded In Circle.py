class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x,y=0,0
        d=(0,1)
        for inst in instructions:
            if inst=='G':
                x,y=x+d[0],y+d[1]
            elif inst=='L':
                d=(-d[1],d[0])
            else:
                d=(d[1],-d[0])
        return (x==0 and y==0) or d!=(0,1)