class Solution:
    def makeFancyString(self, s: str) -> str:
        ans = []
        if len(s)<3:
            return s
        for i in range(0,len(s)-2):
            if s[i]==s[i+1] and s[i]==s[i+2]:
                continue
            ans.append(s[i])
        ans.append(s[len(s)-2])
        ans.append(s[len(s)-1])
        return "".join(ans)
