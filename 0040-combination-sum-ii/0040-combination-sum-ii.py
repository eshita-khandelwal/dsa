class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(i,sum1,subset):
            if sum1 == target:
                res.append(subset.copy())
                return
            if i == len(candidates) or sum1 > target:
                return
            sum1 +=candidates[i]
            subset.append(candidates[i])
            dfs(i+1,sum1,subset)
            sum1 -=candidates[i]
            subset.pop()
            j = i + 1
            while j < len(candidates) and candidates[j] == candidates[i]:
                j += 1
            dfs(j, sum1, subset)
        dfs(0,0,[])
        return res