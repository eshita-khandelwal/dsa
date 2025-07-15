class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def dfs(cur,i):
            res.append(cur.copy())
            for idx in range(i,len(nums)):
                if idx>i and nums[idx] == nums[idx-1]:
                    continue
                cur.append(nums[idx])
                dfs(cur,idx+1)
                cur.pop()
        
        dfs([],0)
        return res