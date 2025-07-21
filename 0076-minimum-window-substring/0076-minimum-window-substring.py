class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count = {}
        for i in t:
            count[i] = 1 + count.get(i,0)
        
        countS = {}
        r=l=0
        res = float("infinity")
        ans = [-1,-1]
        have = 0
        need = len(count)
        while r<len(s):
            countS[s[r]] = 1 + countS.get(s[r],0)
            if s[r] in count and count[s[r]] == countS[s[r]]:
                have+=1
            while have == need:
                if r-l+1<res:
                    res = r-l+1
                    ans[0] = l
                    ans[1] = r
                countS[s[l]]-=1

                if s[l] in count and countS[s[l]]<count[s[l]]:
                    have -=1
                l+=1
            r+=1
        return s[ans[0]:ans[1]+1]


                
