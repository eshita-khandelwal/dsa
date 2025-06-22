class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = []
        for i in s:
            if (i>='a' and i<='z' ) or (i>='A' and  i<='Z') or (i>='0' and i<='9'):
                strs.append(i.lower())
        for i in range(len(strs)):
            if strs[i]!= strs[len(strs)-i-1]:
                return False
        return True