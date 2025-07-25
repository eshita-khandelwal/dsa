class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        res = 0
        l = 0
        c = 0
        for r in range(len(s)):
            if s[r] == 'a' or s[r] == 'e' or s[r] == 'i' or s[r] == 'o' or s[r] == 'u':
                c +=1
            if r-l+1>=k:
                res = max(res,c)
                
                if s[l] == 'a' or s[l] == 'e' or s[l] == 'i' or s[l] == 'o' or s[l] == 'u':
                    c-=1
                l+=1
        return res
                        
                
