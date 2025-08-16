class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        seen = set()
        def dfs(i,sum1,subset):
            if i==len(candidates) or sum1 > target:
                return
            if sum1 == target:
                sorted_subset = tuple(sorted(subset))
                if sorted_subset in seen:
                    return
                res.append(subset.copy())
                seen.add(sorted_subset)
                return
            
            subset.append(candidates[i])
            sum1 +=candidates[i]
            dfs(i,sum1,subset)
            subset.pop()
            sum1 -=candidates[i]
            dfs(i+1,sum1,subset)
        
        
        dfs(0,0,[])
        return res