class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        def dfs(i,sum1,cur):
            nonlocal res
            if sum1==target:
                res.append(cur.copy())
                return
            for idx in range(i,len(nums)):
                if sum1 + nums[idx] > target:
                    break
                if idx > i and nums[idx] == nums[idx-1]:
                    continue
                cur.append(nums[idx])
                dfs(idx+1,sum1+nums[idx],cur)
                cur.pop()
        
        dfs(0,0,[])
        return res