class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        def dfs(nums,res,i):
            nonlocal ans
            if i >= len(nums) or sum(res)>target:
                return 
            if target == sum(res):
                ans.append(res.copy())
                return
            res.append(nums[i])
            dfs(nums,res,i)
            res.pop()
            dfs(nums,res,i+1)

        
        dfs(nums,[],0)
        return list(ans)
