class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        def dfs(i,subset):
            if i == len(nums):
                res.append(subset.copy())
                return
            subset.append(nums[i])
            dfs(i+1,subset)
            subset.pop()
            j = i+1
            while j<len(nums) and nums[j] == nums[j-1]:
                j +=1
            dfs(j,subset)
        
        dfs(0,[])
        return res
