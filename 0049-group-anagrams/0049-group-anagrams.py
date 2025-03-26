class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        s={}
        for i in range(0,len(strs)):
            str1="".join(sorted(strs[i]))
            if str1 not in s:
                s[str1]=[]
            s[str1].append(strs[i])
        return list(s.values())