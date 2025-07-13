class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = {}
        for i in range(len(s)):
            count[s[i]] = 1 + count.get(s[i],0)
        
        for key,val in count.items():
            if val == 1:
                return s.find(key)
        return -1