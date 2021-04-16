class Solution:
    
    def nsl_h(self,heights):
        
        nsl=[]
        stack=[]
        for i in range(len(heights)):
            
            if len(stack)==0:
                nsl.append(-1)
                
            else:
                if stack and stack[-1][0]<heights[i]:
                    nsl.append(stack[-1][1])
                else:
                    
                    while stack and stack[-1][0]>=heights[i]:
                        stack.pop()
                        # if not stack:
                        #     nsl.append(-1)
                        #     stack.append([heights[i],i])
                        #     continue
                    if stack:        
                        nsl.append(stack[-1][1])
                    else:
                        nsl.append(-1)
            stack.append([heights[i],i])
            
        
        return nsl   
        
        
    def nsr_h(self,heights):
        
        nsr=[]
        stack=[]
        for i in range(len(heights)-1,-1,-1):
            
            if len(stack)==0:
                nsr.append(len(heights))
                
            else:
                if stack[-1][0]<heights[i]:
                    nsr.append(stack[-1][1])
                else:
                    
                    while stack and stack[-1][0]>heights[i]:
                        stack.pop()
                        
                    if stack:        
                        nsr.append(stack[-1][1])
                    else:
                        nsr.append(len(heights))
            stack.append([heights[i],i])
            
        nsr=nsr[::-1]
        return nsr
    
            
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        nsl_index=self.nsl_h(heights)
        nsr_index=self.nsr_h(heights)
        width=[0]*(len(heights))

        max_area=0
        for i in range(len(heights)):
            
            
            max_area=max(max_area,(nsr_index[i]-nsl_index[i]-1)*heights[i])
       
        return max_area