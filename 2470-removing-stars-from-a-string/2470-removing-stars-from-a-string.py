class Solution:
    def removeStars(self, s: str) -> str:
        #use stack
        stringStack = []
        
        for i in range(0,len(s)):
            if s[i]!='*':
                stringStack.append(s[i])
                continue
            else:
                if stringStack:
                    stringStack.pop()
        ans = "".join(stringStack)
        
        return ans


