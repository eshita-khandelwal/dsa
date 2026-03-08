class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        res = 0
        store = set()
        for r in range(len(s)):
            while s[r] in store:
                store.remove(s[l])
                l+=1
                
            res=max(res,r-l+1)
            store.add(s[r])
        return res
