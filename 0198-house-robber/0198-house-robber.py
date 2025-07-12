class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        maxAmount = [0 for i in range(len(nums)+1)]
        maxAmount[len(nums)-1] = nums[len(nums)-1]
        for i in range(len(nums)-2,-1,-1):
            maxAmount[i] = max(maxAmount[i+1],maxAmount[i+2] + nums[i])
        
        return maxAmount[0]