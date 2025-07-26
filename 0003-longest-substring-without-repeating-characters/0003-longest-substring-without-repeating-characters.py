class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        r = 0
        l = 0
        count = {}
        while r<len(s):
            while s[r] in count and count[s[r]]!=0:
                count[s[l]] -=1
                l+=1
            count[s[r]] = 1 + count.get(s[r],0)
            res = max(res,r-l+1)
            r+=1
        return res
