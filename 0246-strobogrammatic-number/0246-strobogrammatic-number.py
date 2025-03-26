class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        mirror = {
            "0":"0",
            "1":"1",
            "6":"9",
            "9":"6",
            "8":"8"
        }
        ans = ""
        for i in range(len(num)-1,-1,-1):
            if num[i] not in mirror:
                return False
            ans+=mirror[num[i]]
        
        return ans==num