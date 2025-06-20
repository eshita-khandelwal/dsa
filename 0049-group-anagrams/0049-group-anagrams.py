class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        hashStrs = {}

        for s in strs:
            sortedStr = ''.join(sorted(s))
            if sortedStr in hashStrs:
                hashStrs[sortedStr].append(s)
            else:
                hashStrs[sortedStr] = hashStrs.get(sortedStr, [s])
        
        for key,val in hashStrs.items():
            result.append(val)
        return result