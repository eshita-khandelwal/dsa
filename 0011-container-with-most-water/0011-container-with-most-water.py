class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0
        i = 0
        j=len(height)-1
        maxl = height[0]
        maxr = height[len(height)-1]
        while i<j:
            maxArea = max(maxArea, (j-i) * min(maxl,maxr))
            if maxl < maxr:
                i+=1
                maxl = height[i]
            else:
                j-=1
                maxr = height[j]
            
            
        return maxArea