class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(path,remaining):
            if len(remaining)==0:
                res.append(path)
                return
            for i in range(len(remaining)):
                newremain = remaining[:i] + remaining[i+1:]
                newpath = [remaining[i]] + path
                backtrack(newpath,newremain)

        backtrack([],nums)
        return res