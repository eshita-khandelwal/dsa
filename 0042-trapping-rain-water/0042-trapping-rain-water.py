class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        maxl = [0] * n
        maxr = [0] * n
        minlr = [0] * n
        maxr[n-1]=0
        for i in range(1,n):
            maxl[i] = max(maxl[i-1],height[i-1])
        for i in range(n-2,-1,-1):
            maxr[i] = max(maxr[i+1],height[i+1])
        for i in range(n):
            minlr[i] = min(maxl[i],maxr[i])
        
        ans = 0
        for i in range(n):
            if minlr[i] - height[i]>0:
                ans+=minlr[i] - height[i]
        return ans
