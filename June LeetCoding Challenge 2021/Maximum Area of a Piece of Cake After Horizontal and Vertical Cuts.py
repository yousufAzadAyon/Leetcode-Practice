class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts, verticalCuts) -> int:
        
        horizontalCuts = sorted(horizontalCuts)
        verticalCuts = sorted(verticalCuts)
        
        #adding cake edges
        horizontalCuts.append(h)
        verticalCuts.append(w)
        
        
        #find maximun distance for horizontalCut
        maxHeight = 0
        prevHeigh = 0
        for hCut in horizontalCuts:
            if (hCut - prevHeigh) > maxHeight:
                maxHeight = hCut - prevHeigh
            prevHeigh = hCut
        
        #find maximun distance for vertialCut
        maxWidth = 0
        prevWidth = 0
        for vCut in verticalCuts:
          
            if vCut - prevWidth > maxWidth:
                maxWidth = vCut - prevWidth
            prevWidth = vCut
            
        return (maxHeight * maxWidth) % (10**9 + 7)