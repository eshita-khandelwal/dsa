class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1,max(piles)
        res = sum(piles)
        def canEat(banana):
            hour = 0
            for p in piles:
                hour +=math.ceil(p/banana)
            return hour <= h

        while l<=r:
            m = (r+l)//2
            if canEat(m):
                #print(m)
                r = m-1
                res = min(res,m)
            else:
                l = m+1
        return res