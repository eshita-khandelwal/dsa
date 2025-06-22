class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i=0
        j = 0
        maxl = 0
        set1 = set()
        while j<len(s):
            while s[j] in set1:
                set1.remove(s[i])
                i+=1
            set1.add(s[j])
            maxl = max(maxl,j-i+1)
            j+=1
            
        return maxl
