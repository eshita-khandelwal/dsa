class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1, max(piles) #l and r are the min and max bananas that can be eaten in an hour
        while l < r:
            m = (l+r)//2
            hour_spent = 0
            for pile in piles:
                hour_spent +=math.ceil(pile/m)
            if hour_spent <= h:
                r = m
            else:
                l = m+1
        
        return r

