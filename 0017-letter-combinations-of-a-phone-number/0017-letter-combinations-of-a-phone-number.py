class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        digit_Map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        res = []

        def dfs(i,s):
            if i == len(digits) and len(s) == len(digits):
                res.append(s)
                return
            for j in range(i,len(digits)):
                for k in range(len(digit_Map[digits[j]])):
                    s +=digit_Map[digits[j]][k]
                    dfs(j+1,s)
                    s = s[:-1]
        
        dfs(0,"")
        return res