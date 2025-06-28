class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) == 0 or len(t) ==0:
            return ""
        countT, window = {},{} #hashmap

        for c in t:
            countT[c] = 1 + countT.get(c,0)
        
        l = 0
        res = [-1,-1]
        resl = float("infinity")
        have = 0 
        need = len(countT)

        for r in range(len(s)):
            window[s[r]] = 1 + window.get(s[r],0)
            if s[r] in countT and countT[s[r]] == window[s[r]]:
                have+=1

            while have == need:
                if r-l+1 < resl:
                    resl=r-l+1
                    res = [l,r]
                window[s[l]] -=1
                
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have-=1
                l+=1
        l,r = res
        return s[l:r+1] if resl<float("infinity") else ""


