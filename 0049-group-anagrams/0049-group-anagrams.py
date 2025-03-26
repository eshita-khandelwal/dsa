class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans=[]
        s={}
        for i in range(0,len(strs)):
            str1="".join(sorted(strs[i]))
            print(str1)
            if str1 not in s:
                s[str1]=[]
            s[str1].append(strs[i])
        
        for k,v in s.items():
            ans.append(list(v))
        return ans


